from typing import Annotated
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from core import db_helper
from core.schemas import TeacherRead, TeacherCreate, TeacherUpdate, TeacherUpdatePartial, Teacher
from crud import teachers_crud
from dependencies import teacher_by_id


router = APIRouter(prefix="/teacher", tags=["Teacher"])


@router.get("/", response_model=list[Teacher])
async def get_all_teachers(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    skip: int = Query(0, ge=0), 
    limit: int = Query(10, ge=1),
) -> TeacherRead:
    return await teachers_crud.get_all_teachers(
        session=session,
        skip=skip,
        limit=limit
    )


@router.get("/{entity_id}/", response_model=Teacher)
async def get_teacher(
    teacher: Annotated[TeacherRead, Depends(teacher_by_id)]
) -> TeacherRead:
    return teacher



@router.post("/", response_model=TeacherRead, status_code=status.HTTP_201_CREATED)
async def create_taecher(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    teacher_in: TeacherCreate
) -> TeacherRead:
    return await teachers_crud.create_teacher(
        session=session, teacher_in=teacher_in
    )


@router.put("/{entity_id}/", response_model=Teacher)
async def update_teacher(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    update_teacher: TeacherUpdate,
    teacher: Annotated[TeacherRead, Depends(teacher_by_id)]
) -> TeacherRead:
    return await teachers_crud.update_teacher(
        session=session, 
        update_teacher=update_teacher, 
        teacher=teacher
    )


@router.patch("/{entity_id}/", response_model=Teacher)
async def update_teacher_partial(
    teacher: Annotated[TeacherRead, Depends(teacher_by_id)],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    update_teacher: TeacherUpdatePartial,
) -> TeacherRead:
    return await teachers_crud.update_teacher(
        session=session, 
        update_teacher=update_teacher, 
        teacher=teacher,
        partial=True
    )


@router.delete("/{entity_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_teacher(
    teacher: Annotated[TeacherRead, Depends(teacher_by_id)],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
) -> None:
    return await teachers_crud.delete_teacher(
        teacher=teacher,
        session=session
    )