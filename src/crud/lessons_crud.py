from typing import Sequence
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Lesson
from core.schemas import LessonCreate, LessonUpdate, LessonUpdatePartial, LessonRead


async def get_all_lessons_with_subjects(
    session: AsyncSession,
    limit: int,
    skip: int
) -> Sequence[Lesson]:
    stmt = (
        select(Lesson).options(joinedload(Lesson.subject)).offset(skip).limit(limit).order_by(Lesson.id)
    )
    lessons = await session.scalars(stmt)
    return lessons.all()


async def get_lesson(
    session: AsyncSession,
    entity_id: int
) -> Lesson | None:
    stmt = (
        select(Lesson).options(joinedload(Lesson.subject)).where(Lesson.id==entity_id)
    )
    lesson = await session.scalars(stmt)
    return lesson.one_or_none()


async def create_lesson(
    session: AsyncSession,
    lesson_in: LessonCreate
) -> LessonRead:
    lesson = Lesson(**lesson_in.model_dump())
    session.add(lesson)
    await session.commit()
    return lesson


async def update_lesson(
    session: AsyncSession,
    lesson_update: LessonUpdate | LessonUpdatePartial,
    lesson: Lesson,
    partial: bool = False
) -> Lesson:
    for name, value in lesson_update.model_dump(exclude_unset=partial).items():
        setattr(lesson, name, value)
    await session.commit()
    return lesson


async def delete_lesson(
    session: AsyncSession,
    lesson: Lesson
) -> Lesson:
    await session.delete(lesson)
    await session.commit()