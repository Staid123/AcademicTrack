from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import StudentSubjectAssociation as Grade, Subject
from core.schemas import GradeUpdate, GradeUpdatePartial, GradeCreate, GradeRead


async def get_all_grades_with_student_subject_semester(
    session: AsyncSession,
    limit: int,
    skip: int
) -> list[Grade]:
    stmt = (
        select(Grade)
        .options(
            joinedload(Grade.student),
            joinedload(Grade.subject).joinedload(Subject.teacher),
            joinedload(Grade.semester)
        )
        .offset(skip)
        .limit(limit)
        .order_by(Grade.id)
    )
    grades = await session.scalars(stmt)
    return grades.all()



async def get_grade(
    entity_id: int,
    session: AsyncSession
) -> Grade | None:
    stmt = (
        select(Grade)
        .options(
            joinedload(Grade.student),
            joinedload(Grade.subject).joinedload(Subject.teacher),
            joinedload(Grade.semester)
        )
        .where(Grade.id==entity_id)
    )
    grade = await session.scalars(stmt)
    return grade.one_or_none()


async def create_grade(
    session: AsyncSession,
    grade_in: GradeCreate
) -> GradeRead:
    grade = Grade(**grade_in.model_dump())
    session.add(grade)
    await session.commit()
    return grade


async def update_grade(
    session: AsyncSession,
    grade: Grade,
    grade_update: GradeUpdate | GradeUpdatePartial,
    partial: bool = False
) -> Grade:
    for name, value in grade_update.model_dump(exclude_unset=partial).items():
        setattr(grade, name, value)
    await session.commit()
    return grade


async def delete_grade(
    session: AsyncSession,
    grade: Grade
) -> None:
    await session.delete(grade)
    await session.commit()
