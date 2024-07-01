from typing import Sequence
from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Subject
from core.schemas import SubjectCreate, SubjectUpdate, SubjectUpdatePartial


async def get_all_subjects(
    session: AsyncSession,
    limit: int,
    skip: int
) -> Sequence[Subject]:
    stmt = select(Subject).options(joinedload(Subject.teacher), selectinload(Subject.lessons)).offset(skip).limit(limit).order_by(Subject.id)
    subjects = await session.scalars(stmt)
    return subjects.all()


async def get_subject(
    session: AsyncSession,
    entity_id: int
) -> Subject | None:
    stmt = (
        select(Subject).options(joinedload(Subject.teacher)).where(Subject.id==entity_id)
    )
    subject = await session.scalars(stmt)
    return subject.one_or_none()


async def create_subject(
    session: AsyncSession,
    subject_in: SubjectCreate
) -> Subject:
    subject = Subject(
        name=subject_in.name,
        teacher_id=subject_in.teacher_id,
        exam_date=subject_in.exam_date.replace(tzinfo=None)  # Убираем временную зону
    )
    session.add(subject)
    await session.commit()
    return subject


async def update_subject(
    session: AsyncSession,
    subject_update: SubjectUpdate | SubjectUpdatePartial,
    subject: Subject,
    partial: bool = False
) -> Subject:
    for name, value in subject_update.model_dump(exclude_unset=partial).items():
        if name == "exam_date":
            exam_date = subject_update.exam_date.replace(tzinfo=None)
            setattr(subject, name, exam_date)
        else:
            setattr(subject, name, value)
    await session.commit()
    return subject


async def delete_subject(
    session: AsyncSession,
    subject: Subject
) -> None:
    await session.delete(subject)
    await session.commit()