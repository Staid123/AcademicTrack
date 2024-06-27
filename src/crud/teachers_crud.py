from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Teacher
from core.schemas import TeacherCreate, TeacherUpdate, TeacherUpdatePartial


async def get_all_teachers(
    session: AsyncSession,
    skip: int = 0,
    limit: int = 10,
) -> Teacher:
    stmt = select(Teacher).offset(skip).limit(limit).order_by(Teacher.id)
    teachers = await session.scalars(stmt)
    return teachers.all()


async def get_teacher(
    session: AsyncSession,
    entity_id: int
) -> Teacher:
    return await session.get(Teacher, entity_id)


async def create_teacher(
    session: AsyncSession,
    teacher_in: TeacherCreate
) -> Teacher:
    teacher = Teacher(**teacher_in.model_dump())
    session.add(teacher)
    await session.commit()
    return teacher