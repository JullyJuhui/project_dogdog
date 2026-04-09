from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.domains.auth.api.app_api import router as app_router
from backend.app.domains.products.products_api import router as products_router
from backend.app.domains.pets.pets_api import router as pets_router

# FastAPI 앱 생성
app = FastAPI(
    title="DogDog Backend",
    description="앱/ERP 공통 백엔드 서버",
    version="1.0.0"
)

# CORS 설정
# 프론트와 백엔드가 서로 다른 주소/포트를 쓸 때 요청 허용을 위한 설정입니다.
# 지금은 테스트 단계이므로 모두 허용(*) 처리합니다.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# auth 라우터 등록
# 예: app_api.py 안에 @router.post("/user") 가 있으면 최종 주소는 /app/user
app.include_router(app_router, prefix="/app")

# 상품 라우터 등록
app.include_router(pets_router, prefix="/app")

# 상품 라우터 등록
app.include_router(products_router, prefix="/app")