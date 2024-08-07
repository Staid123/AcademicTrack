from .api_v1.semester import router as semester_router
from .api_v1.student import router as student_router
from .api_v1.group import router as group_router
from .api_v1.teacher import router as teacher_router
from .api_v1.subject import router as subject_router
from .api_v1.lesson import router as lesson_router
from .api_v1.daily_schedule import router as daily_schedule_router
from .api_v1.weekly_schedule import router as weekly_schedule_router
from .api_v1.grade import router as grade_router

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

router.include_router(
    router=teacher_router
)

router.include_router(
    router=subject_router
)

router.include_router(
    router=lesson_router
)

router.include_router(
    router=daily_schedule_router
)

router.include_router(
    router=weekly_schedule_router
)

router.include_router(
    router=grade_router
)