from sqlalchemy import select
from sqlalchemy.orm import Session

from database.models import CompanionPet, CompanionPetFood, CompanionButler, CompanionPetProductFeeding, OpdProduct

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
        select(CompanionPetProductFeeding.product_id)
        .where(
            CompanionPetProductFeeding.pet_id == pet_id,
            CompanionPetProductFeeding.is_feeding_check == True
        )
    )
    result = db.execute(query)
    feeding_product = result.one() # 내맘대로 쓴거 ㅎㅎ
    return feeding_product

# 기존 활성 사료 종료 = 삭제
def deactivate_pet_food(db: Session, pet_food: PetProductFeeding, feeding_false_date):
    pet_food.is_feeding_check = False
    pet_food.feeding_false_date = feeding_false_date

# --------------- 등록 ---------------
def insert_pet_food(
    db: Session,
    total_weight: int
):
    new_PetFood = CompanionPetFood(
        total_weight=total_weight
    )

    db.add(new_PetFood)
    return new_PetFood

def insert_pet_food(
    db: Session,
    pet_id: int,
    product_id: int,
    one_gram_calories: float
):
    new_PetProductFeeding = CompanionPetProductFeeding(
        pet_id=pet_id,
        product_id=product_id,
        one_gram_calories=one_gram_calories,
    )

    db.add(new_PetProductFeeding)
    return new_PetProductFeeding

# 새 급여 사료 row 생성
def insert_pet_product_feeding(
    db: Session,
    pet_id: int,
    product_id: int,
    one_gram_calories: float
):
    new_PetProductFeeding = CompanionPetProductFeeding(
        pet_id=pet_id,
        product_id=product_id,
        one_gram_calories=one_gram_calories,
    )

    db.add(new_PetProductFeeding)
    return new_PetProductFeeding