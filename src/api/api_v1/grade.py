from typing import Annotated
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from core import db_helper
from core.schemas import Grade, GradeUpdate, GradeCreate, GradeRead, GradeUpdatePartial
from crud import grades_crud
from dependencies import grade_by_id


router = APIRouter(prefix="/grade", tags=["Grade"])


@router.get("/", response_model=list[Grade])
async def get_all_grades_with_students_subjects_semesters(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    skip: int = Query(0, ge=0), 
    limit: int = Query(10, ge=1),
) -> list[Grade]:
    return await grades_crud.get_all_grades_with_student_subject_semester(
        session=session,
        skip=skip,
        limit=limit
    )


@router.get("/{enity_id}/", response_model=Grade)
async def get_grade(
    grade: Annotated[Grade, Depends(grade_by_id)]
) -> Grade:
    return grade


@router.post("/", response_model=GradeRead, status_code=status.HTTP_201_CREATED)
async def create_grade(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    grade_in: GradeCreate
) -> GradeRead:
    return await grades_crud.create_grade(
        session=session,
        grade_in=grade_in
    )


@router.put("/{entity_id}/", response_model=Grade)
async def update_grade(
    grade: Annotated[Grade, Depends(grade_by_id)],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    grade_update: GradeUpdate
) -> Grade:
    return await grades_crud.update_grade(
        grade=grade,
        grade_update=grade_update,
        session=session
    )


@router.patch("/{entity_id}/", response_model=Grade)
async def update_grade_partial(
    grade: Annotated[Grade, Depends(grade_by_id)],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    grade_update: GradeUpdatePartial
) -> Grade:
    return await grades_crud.update_grade(
        grade=grade,
        grade_update=grade_update,
        session=session,
        partial=True
    )

@router.delete("/{entity_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_grade(
    grade: Annotated[Grade, Depends(grade_by_id)],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
) -> None:
    return await grades_crud.delete_grade(
        grade=grade,
        session=session
    )