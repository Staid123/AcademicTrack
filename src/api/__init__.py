from .api_v1.semester import router as semester_router
from .api_v1.student import router as student_router
from .api_v1.group import router as group_router
from fastapi import APIRouter

router = APIRouter(prefix="/v1")

router.include_router(
    router=semester_router
)

router.include_router(
    router=student_router
)

router.include_router(
    router=group_router
)

