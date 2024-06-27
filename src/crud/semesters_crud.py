from typing import Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Semester
from core.schemas import SemesterCreate, SemesterUpdate, SemesterUpdatePartial


async def get_all_semesters(
    session: AsyncSession, 
    skip: int = 0, 
    limit: int = 0
) -> Sequence[Semester]:
    stmt = select(Semester).offset(skip).limit(limit).order_by(Semester.id)
    result = await session.scalars(stmt)
    return result.all()


async def get_semester(
    session: AsyncSession,
    entity_id: int
) -> Semester | None:
    return await session.get(Semester, entity_id)


async def create_semester(
    session: AsyncSession, 
    semester_in: SemesterCreate
) -> Semester:
    semester = Semester(**semester_in.model_dump())
    session.add(semester)
    await session.commit()
    return semester


async def update_semester(
    session: AsyncSession,
    semester: Semester,
    semester_update: SemesterUpdate | SemesterUpdatePartial,
    partial: bool = False,
) -> Semester:
    for name, value in semester_update.model_dump(exclude_unset=partial).items():
        setattr(semester, name, value)
    await session.commit()
    return semester


async def delete_semester(
    session: AsyncSession,
    semester: Semester
) -> None:
    await session.delete(semester)
    await session.commit()