from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Teacher
from core.schemas import TeacherCreate, TeacherUpdate, TeacherUpdatePartial


async def get_all_teachers(
    session: AsyncSession,
    skip: int = 0,
    limit: int = 10,
) -> Teacher:
    stmt = select(Teacher).options(selectinload(Teacher.subjects)).offset(skip).limit(limit).order_by(Teacher.id)
    teachers = await session.scalars(stmt)
    return teachers.all()


async def get_teacher(
    session: AsyncSession,
    entity_id: int
) -> Teacher:
    stmt = select(Teacher).options(selectinload(Teacher.subjects)).where(Teacher.id==entity_id)
    teacher = await session.scalars(stmt)
    return teacher.one_or_none()


async def create_teacher(
    session: AsyncSession,
    teacher_in: TeacherCreate
) -> Teacher:
    teacher = Teacher(**teacher_in.model_dump())
    session.add(teacher)
    await session.commit()
    return teacher


async def update_teacher(
    session: AsyncSession,
    update_teacher: TeacherUpdate | TeacherUpdatePartial,
    teacher: Teacher,
    partial: bool = False
) -> Teacher:
    for name, value in update_teacher.model_dump(exclude_unset=partial).items():
        setattr(teacher, name, value)
    await session.commit()
    return teacher


async def delete_teacher(
    session: AsyncSession,
    teacher: Teacher
) -> None:
    await session.delete(teacher)
    await session.commit()