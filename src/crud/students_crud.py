from typing import Sequence
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Student
from core.schemas import StudentCreate, StudentUpdate, StudentUpdatePartial
from exceptions import student_not_found


async def get_all_students(
    session: AsyncSession,
    skip: int = 0,
    limit: int = 10,
) -> Sequence[Student]:
    stmt = select(Student).options(joinedload(Student.group)).offset(skip).limit(limit).order_by(Student.id)
    result = await session.scalars(stmt)
    return result.all()


async def get_student(
    session: AsyncSession,
    entity_id: int
) -> Student | None:
    student = await session.get(Student, entity_id)
    return student 


async def get_student_with_group(
    session: AsyncSession,
    student_id: int
):
    stmt = (
        select(Student).options(joinedload(Student.group)).where(Student.id==student_id)
    )
    result = await session.scalars(stmt)
    student = result.one_or_none()
    if student:
        return student 
    raise student_not_found(student_id)


async def create_student(
    session: AsyncSession,
    student_in: StudentCreate
) -> Student:
    student = Student(**student_in.model_dump())
    session.add(student)
    await session.commit()
    return student


async def update_student(
    session: AsyncSession,
    student_update: StudentUpdate | StudentUpdatePartial,
    student: Student,
    partial: bool = False
) -> Student:
    for name, value in student_update.model_dump(exclude_unset=partial).items():
        setattr(student, name, value)
    await session.commit()
    return student


async def delete_student(
    session: AsyncSession,
    student: Student
) -> None:
    await session.delete(student)
    await session.commit()

