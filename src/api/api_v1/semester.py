from typing import Annotated
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from core import db_helper
from core.schemas import SemesterCreate, Semester, SemesterUpdate, SemesterUpdatePartial
from crud import semesters_crud
from dependencies import semester_by_id

router = APIRouter(prefix="/semester", tags=["Semester"])


@router.get("/", response_model=list[Semester])
async def get_all_semesters(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    skip: int = Query(0, ge=0), 
    limit: int = Query(10, ge=1),
) -> list[Semester]:
    semesters = await semesters_crud.get_all_semesters(
        session=session, 
        skip=skip, 
        limit=limit
    )
    return semesters


@router.get("/{semester_id}/", response_model=Semester)
async def get_semester(
    semester: Semester = Depends(semester_by_id),
) -> Semester:
    return semester


@router.post(
    "/", 
    response_model=Semester,
    status_code=status.HTTP_201_CREATED
)
async def create_semester(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    semester_in: SemesterCreate,
) -> Semester:
    return await semesters_crud.create_semester(session=session, semester_in=semester_in)



@router.put("/{semester_id}/", response_model=Semester)
async def update_semester(
    semester_update: SemesterUpdate,
    semester: Semester = Depends(semester_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
) -> Semester:
    return await semesters_crud.update_semester(
        session=session,
        semester=semester,
        semester_update=semester_update,
    )


@router.patch("/{semester_id}/", response_model=Semester)
async def update_semester_partial(
    semester_update: SemesterUpdatePartial,
    semester: Semester = Depends(semester_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
) -> Semester:
    return await semesters_crud.update_semester(
        session=session,
        semester=semester,
        semester_update=semester_update,
        partial=True
    )


@router.delete("/{semester_id}/")
async def delete_semester(
    semester: Semester = Depends(semester_by_id),
    session: AsyncSession = Depends(db_helper.session_getter)
) -> None:
    await semesters_crud.delete_semester(session=session, semester=semester)