from .api_v1.semester import router as semester_router
from fastapi import APIRouter

router = APIRouter(prefix="/v1")

router.include_router(
    router=semester_router
)