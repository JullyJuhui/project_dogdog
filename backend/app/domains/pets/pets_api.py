from fastapi import APIRouter, Depends, Body
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from database.db import get_db
from backend.app.domains.pets.petFood_service import create_pet_food
from backend.app.core.auth import get_current_customer_id  # 가정: 토큰에서 customer_id 추출

router = APIRouter(tags=["pets"])


@router.post("/pets/{pet_id}/pet_food")
def register_pet_food(
    pet_id: int,
    body: dict = Body(...),
    db: Session = Depends(get_db),
    customer_id: int = Depends(get_current_customer_id)
):
    """
    로그인한 사용자의 반려견에게 현재 급여 중인 사료를 등록한다.
    기존 활성 사료가 있으면 종료 처리 후 새 사료를 등록한다.
    """
    try:
        product_id = body.get("product_id")
        total_weight = body.get("total_weight")
        left_intake = body.get("left_intake")

        result = create_pet_food(
            db=db,
            customer_id=customer_id,
            pet_id=pet_id,
            product_id=product_id,
            total_weight=total_weight,
            left_intake=left_intake
        )

        return {
            "success": True,
            "message": "급여 사료가 등록되었습니다.",
            "data": result
        }

    except ValueError as e:
        error_code = str(e)

        error_map = {
            "PRODUCT_ID_REQUIRED": (400, "상품 ID는 필수입니다."),
            "TOTAL_WEIGHT_REQUIRED": (400, "총 무게는 필수입니다."),
            "LEFT_INTAKE_REQUIRED": (400, "사료 잔여량은 필수입니다."),
            "INVALID_TOTAL_WEIGHT": (422, "총 무게는 0보다 커야 합니다."),
            "INVALID_LEFT_INTAKE": (422, "사료 잔여량은 0 이상이어야 합니다."),
            "PET_NOT_FOUND": (404, "존재하지 않는 반려견입니다."),
            "PRODUCT_NOT_FOUND": (404, "존재하지 않는 사료입니다."),
            "FORBIDDEN_PET_ACCESS": (403, "해당 반려견에 대한 권한이 없습니다."),
            "PRODUCT_CALORIES_NOT_FOUND": (404, "상품 칼로리 정보가 없습니다."),
        }

        status_code, message = error_map.get(
            error_code,
            (400, "잘못된 요청입니다.")
        )

        return JSONResponse(
            status_code=status_code,
            content={
                "success": False,
                "error_code": error_code,
                "message": message
            }
        )

    except Exception as e:
        print("급여 사료 등록 실패:", e)

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "error_code": "PET_FOOD_CREATE_FAILED",
                "message": "사료 정보 저장에 실패했습니다."
            }
        )