from datetime import date
from sqlalchemy.orm import Session

from backend.app.domains.pets.petFood_repository import (
    get_pet_by_id,
    check_pet_owner,
    get_product_by_id,
    get_active_pet_food,
    deactivate_pet_food,
    insert_customer_food,
    insert_pet_product_feeding
)

def create_pet_food(
    db: Session,
    customer_id: int,
    pet_id: int,
    product_id: int | None,
    total_weight: int | None,
):
    """
    반려견의 현재 급여 사료를 등록한다.

    처리 순서:
    1. 입력값 검증
    2. pet 존재 확인
    3. 로그인 사용자 권한 확인
    4. product 존재 확인
    5. 기존 활성 사료 종료 처리
    6. 새 급여 사료 row 생성
    """
    # 1. 입력값 검증
    if product_id is None:
        raise ValueError("PRODUCT_ID_REQUIRED")

    if total_weight is None:
        raise ValueError("TOTAL_WEIGHT_REQUIRED")

    # if left_intake is None:
    #     raise ValueError("LEFT_INTAKE_REQUIRED")

    if total_weight <= 0:
        raise ValueError("INVALID_TOTAL_WEIGHT")

    # if left_intake < 0:
    #     raise ValueError("INVALID_LEFT_INTAKE")
    
    # 필요하면 left_intake <= total_weight 검증도 가능
    # if left_intake > total_weight:
    #     raise ValueError("INVALID_LEFT_INTAKE")

    # 2. pet 존재 확인
    pet = get_pet_by_id(db=db, pet_id=pet_id)
    if pet is None:
        raise ValueError("PET_NOT_FOUND")

    # 3. 권한 확인
    has_access = check_pet_owner(
        db=db,
        pet_id=pet_id,
        customer_id=customer_id
    )
    if not has_access:
        raise ValueError("FORBIDDEN_PET_ACCESS")

    # 4. product 존재 확인
    product = get_product_by_id(db=db, product_id=product_id)
    if product is None:
        raise ValueError("PRODUCT_NOT_FOUND")

    if product.product_detail.calories is None:
        raise ValueError("PRODUCT_CALORIES_NOT_FOUND")

    # 5. 기존 활성 사료 종료 처리
    active_food = get_active_pet_food(db=db, pet_id=pet_id)
    if active_food is not None:
        deactivate_pet_food(
            db=db,
            pet_food=active_food,
            feeding_false_date=date.today()
        )

    # 6. 새 사료 등록
    # 잔여량 등록
    new_CustomerFood = insert_customer_food(
        db=db,
        pet_id=pet_id,
        total_weight=total_weight
    )

    # 사료 등록
    new_PetProductFeeding = insert_pet_product_feeding(
        db=db,
        pet_id=pet_id,
        product_id=product_id,
        one_gram_calories=product.product_detail.calories
    )

    db.commit()
    db.refresh(new_CustomerFood)
    db.refresh(new_PetProductFeeding)

    # left_weight_g = total_weight - left_intake

    return {
        "pet_id": new_PetProductFeeding.pet_id,
        "product_id": new_PetProductFeeding.product_id,
        "product_name": product.product_detail.product_name,
        "total_weight_g": new_CustomerFood.total_weight,
        "one_gram_calories": new_PetProductFeeding.one_gram_calories,
        "is_feeding_check": new_PetProductFeeding.is_feeding_check,
        "record_date": str(new_PetProductFeeding.record_date)
    }