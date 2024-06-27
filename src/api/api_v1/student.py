from typing import Annotated
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from core import db_helper
from core.schemas import Student, StudentCreate, StudentUpdate, StudentUpdatePartial, StudentWithGroup
from crud import students_crud
from dependencies import student_by_id


router = APIRouter(prefix="/student", tags=["Student"])


@router.get("/with_group/", response_model=list[StudentWithGroup])
async def get_all_students_with_groups(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    skip: int = Query(0, ge=0), 
    limit: int = Query(10, ge=1),
) -> list[StudentWithGroup]:
    students = await students_crud.get_all_students(
        session=session,
        skip=skip,
        limit=limit
    )
    return students


@router.get("/", response_model=list[Student])
async def get_all_students(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    skip: int = Query(0, ge=0), 
    limit: int = Query(10, ge=1),
) -> list[Student]:
    students = await students_crud.get_all_students(
        session=session,
        skip=skip,
        limit=limit
    )
    return students


@router.get("/{entity_id}/", response_model=Student)
async def get_student(
    student: Annotated[Student, Depends(student_by_id)]
) -> Student:
    return student
    


@router.get("/{entity_id}/with_group/", response_model=StudentWithGroup)
async def get_student_with_group(
    student_id: int,
    session: AsyncSession = Depends(db_helper.session_getter),
) -> StudentWithGroup:
    return await students_crud.get_student_with_group(session=session, student_id=student_id)
    

@router.post(
    "/", 
    response_model=Student,
    status_code=status.HTTP_201_CREATED
)
async def create_student(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    student_in: StudentCreate
) -> Student:
    return await students_crud.create_student(session=session, student_in=student_in)


@router.put("/{entity_id}/", response_model=Student)
async def update_student(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    student_update: StudentUpdate,
    student: Student = Depends(student_by_id),
) -> Student:
    return await students_crud.update_student(
        session=session, 
        student_update=student_update, 
        student=student
    )
    

@router.patch("/{entity_id}/", response_model=Student)
async def update_student_partial(
    student_update: StudentUpdatePartial,
    student: Student = Depends(student_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
) -> Student:
    return await students_crud.update_student(
        session=session, 
        student_update=student_update, 
        student=student,
        partial=True
    )
    

@router.delete("/{entity_id}/")
async def delete_student(
    student: Student = Depends(student_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
) -> None:
    return await students_crud.delete_student(session=session, student=student)


