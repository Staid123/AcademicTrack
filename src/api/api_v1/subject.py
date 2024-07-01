from typing import Annotated
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from core import db_helper
from core.schemas import Subject, SubjectCreate, SubjectUpdate, SubjectUpdatePartial, SubjectRead
from crud import subjects_crud
from dependencies import subject_by_id


router = APIRouter(prefix="/subject", tags=["Subject"])


@router.get("/", response_model=list[Subject])
async def get_all_subjects(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    skip: int = Query(0, ge=0), 
    limit: int = Query(10, ge=1),
) -> list[Subject]:
    return await subjects_crud.get_all_subjects(
        session=session,
        limit=limit,
        skip=skip
    )


@router.get("/{entity_id}/", response_model=Subject)
async def get_subject(
    subject: Annotated[Subject, Depends(subject_by_id)]
) -> Subject:
    return subject


@router.post("/", response_model=SubjectRead, status_code=status.HTTP_201_CREATED)
async def create_subject(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    subject_in: SubjectCreate
) -> SubjectRead:
    return await subjects_crud.create_subject(
        session=session,
        subject_in=subject_in
    )


@router.put("/{entity_id}/", response_model=Subject)
async def update_subject(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    subject_update: SubjectUpdate,
    subject: Annotated[Subject, Depends(subject_by_id)] 
) -> Subject:
    return await subjects_crud.update_subject(
        session=session,
        subject_update=subject_update,
        subject=subject
    )


@router.patch("/{entity_id}/", response_model=Subject)
async def update_subject_partial(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    subject: Annotated[Subject, Depends(subject_by_id)],
    subject_update: SubjectUpdatePartial,
) -> Subject:
    return await subjects_crud.update_subject(
        session=session,
        subject_update=subject_update,
        subject=subject,
        partial=True
    )


@router.delete("/{entity_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_subject(
    subject: Annotated[Subject, Depends(subject_by_id)],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
) -> None:
    return await subjects_crud.delete_subject(
        session=session,
        subject=subject
    )