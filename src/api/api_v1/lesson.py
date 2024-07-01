from typing import Annotated
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from core import db_helper
from core.schemas import Lesson, LessonCreate, LessonUpdate, LessonUpdatePartial, LessonRead
from crud import lessons_crud
from dependencies import lesson_by_id


router = APIRouter(prefix="/lesson", tags=["Lesson"])


@router.get("/", response_model=list[Lesson])
async def get_all_lessons_with_subjects(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    skip: int = Query(0, ge=0), 
    limit: int = Query(10, ge=1),
) -> list[Lesson]:
    return await lessons_crud.get_all_lessons_with_subjects(
        session=session,
        skip=skip,
        limit=limit
    )


@router.get("/{entity_id}/", response_model=Lesson)
async def get_lesson_with_subject(
    lesson: Annotated[Lesson, Depends(lesson_by_id)]
) -> Lesson | None:
    return lesson


@router.post("/", response_model=LessonRead, status_code=status.HTTP_201_CREATED)
async def create_lesson(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    lesson_in: LessonCreate
) -> LessonRead:
    return await lessons_crud.create_lesson(
        session=session,
        lesson_in=lesson_in
    )


@router.put("/{entity_id}/", response_model=Lesson)
async def update_lesson(
    lesson: Annotated[Lesson, Depends(lesson_by_id)],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    lesson_update: LessonUpdate
) -> Lesson:
    return await lessons_crud.update_lesson(
        session=session,
        lesson=lesson,
        lesson_update=lesson_update
    )


@router.patch("/{entity_id}/", response_model=Lesson)
async def update_lesson_partial(
    lesson: Annotated[Lesson, Depends(lesson_by_id)],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    lesson_update: LessonUpdatePartial
) -> Lesson:
    return await lessons_crud.update_lesson(
        session=session,
        lesson=lesson,
        lesson_update=lesson_update,
        partial=True
    )


@router.delete("/{entity_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_lesson(
    lesson: Annotated[Lesson, Depends(lesson_by_id)],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
) -> None:
    return await lessons_crud.delete_lesson(
        session=session,
        lesson=lesson
    )