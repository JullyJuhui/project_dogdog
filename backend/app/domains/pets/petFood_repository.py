from sqlalchemy import select
from sqlalchemy.orm import Session

from database.models import CompanionPet, CompanionCustomerFood, CompanionButler, CompanionPetProductFeeding, OpdProduct

from datetime import date

# 존재하는 펫인지 확인
# 펫아이디 가져오기
def get_pet_by_id(db: Session, pet_id: int):
    query = (select(CompanionPet)
             .where(CompanionPet.pet_id == pet_id))
    result = db.execute(query)
    
    return result.scalar_one_or_none()

# 로그인 사용자가 해당 반려견의 보호자인지 확인
# Butler row 존재 여부 가져오기
def check_pet_owner(db: Session, pet_id: int, customer_id: int) -> bool:
    query = (
        select(CompanionButler)
        .where(
            CompanionButler.pet_id == pet_id,
            CompanionButler.customer_id == customer_id,
            CompanionButler.active == True
        )
    )
    result = db.execute(query)
    butler = result.scalar_one_or_none()
    return butler is not None  # T/F

# 존재하는 사료인지 확인
def get_product_by_id(db: Session, product_id: int):
    query = (select(OpdProduct)
             .where(OpdProduct.product_id == product_id))
    result = db.execute(query)
    return result.scalar_one_or_none()

# 현재 반려견이 먹고 있는 active=true 사료 조회
def get_active_pet_food(db: Session, pet_id: int):
    query = (
        # select(CompanionPetProductFeeding.product_id)
        select(CompanionPetProductFeeding)
        .where(
            CompanionPetProductFeeding.pet_id == pet_id,
            # 주석 해제 예정*********************************************
            # CompanionPetProductFeeding.is_feeding_check == True
        )
    )
    result = db.execute(query)
    feeding_product = result.scalar_one_or_none() 
    return feeding_product

# 기존 활성 사료 종료 = 삭제
def deactivate_pet_food(db: Session, pet_food: CompanionPetProductFeeding, feeding_false_date):
    pet_food.is_feeding_check = False
    pet_food.feeding_false_date = feeding_false_date

# 기존 customer_food 등록자인지 확인
def get_customer_food_id(
    db: Session,
    pet_id: int,
):
    query = (
        select(CompanionCustomerFood)
        .where(CompanionCustomerFood.pet_id == pet_id)
    )

    result = db.execute(query)
    return result.scalar_one_or_none()

# ------------------------------ 등록 ------------------------------
def insert_customer_food(
    db: Session,
    pet_id: int,
    total_weight: int
):
    customer_food = get_customer_food_id(db=db, pet_id=pet_id)
    if customer_food is None:
        customer_food = CompanionCustomerFood(
            pet_id=pet_id,
            total_weight=total_weight
            # feeding_start=f"{date.today()}"
        )
        db.add(customer_food)

    # 이미 급여한적이 있는 사용자의 경우 update total_weight
    else:
        customer_food.total_weight = total_weight
        customer_food.feeding_start = date.today()
        # customer_food.total_intake = 0
        # customer_food.left_intake = total_weight
    return customer_food





def insert_pet_product_feeding(
    db: Session,
    pet_id: int,
    product_id: int,
    one_gram_calories: float
):
    pet_product_feeding = get_active_pet_food(db=db, pet_id=pet_id)
    
    # 첫 사료등록인 경우 = pet_id에 대한 row가 존재 하지 않는 경우
    if pet_product_feeding is None:
        pet_product_feeding = CompanionPetProductFeeding(
            pet_id=pet_id,
            product_id=product_id,
            one_gram_calories=one_gram_calories,
        )
        db.add(pet_product_feeding)

    # 새 급여 사료 row 생성
    # 이미 존재하는 경우
    # 변경하려는 사료가 기존 사료와 같은지 비교 --------------> 에러처리 필요
    # false 처리 -> json으로 결과 넘기고 update
    else:
        pet_product_feeding.is_feeding_check = True
        pet_product_feeding.product_id = product_id,
        pet_product_feeding.one_gram_calories = one_gram_calories
    
    return pet_product_feeding