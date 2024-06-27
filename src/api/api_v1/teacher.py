from typing import Annotated
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from core import db_helper
from core.schemas import Teacher, TeacherCreate, TeacherUpdate, TeacherUpdatePartial
from crud import teachers_crud
from dependencies import teacher_by_id


router = APIRouter(prefix="/teacher", tags=["Teacher"])


@router.get("/", response_model=list[Teacher])
async def get_all_teachers(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    skip: int = Query(0, ge=0), 
    limit: int = Query(10, ge=1),
) -> Teacher:
    return await teachers_crud.get_all_teachers(
        session=session,
        skip=skip,
        limit=limit
    )


@router.get("/{entity_id}/", response_model=Teacher)
async def get_teacher(
    teacher: Annotated[Teacher, Depends(teacher_by_id)]
) -> Teacher:
    return teacher



@router.post("/", response_model=Teacher, status_code=status.HTTP_201_CREATED)
async def create_taecher(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    teacher_in: TeacherCreate
) -> Teacher:
    return await teachers_crud.create_teacher(
        session=session, teacher_in=teacher_in
    )