from typing import Annotated
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from core import db_helper
from core.schemas import Group, GroupWithStudents, GroupCreate, GroupUpdate, GroupUpdatePartial
from crud import groups_crud
from dependencies import group_by_id


router = APIRouter(prefix="/group", tags=["Group"])


@router.get("/", response_model=list[GroupWithStudents])
async def get_all_groups_with_students(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    skip: int = Query(0, ge=0), 
    limit: int = Query(10, ge=1),
) -> list[GroupWithStudents]:
    return await groups_crud.get_groups_with_students(
        session=session, limit=limit, skip=skip
    )


@router.get("/{entity_id}/", response_model=GroupWithStudents)
async def get_group_with_students(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    entity_id: int
) -> GroupWithStudents:
    return await groups_crud.get_group(
        session=session, 
        entity_id=entity_id
    )


@router.post("/", response_model=Group)
async def create_group(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    group_in: GroupCreate
) -> Group:
    return await groups_crud.create_group(
        session=session,
        group_in=group_in
    )


@router.put("/{entity_id}/", response_model=Group)
async def update_group(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    update_group: GroupUpdate,
    group: Annotated[Group, Depends(group_by_id)]
) -> Group:
    return await groups_crud.update_group(
        session=session,
        update_group=update_group,
        group=group
    )


@router.patch("/{entity_id}/", response_model=Group)
async def update_group_partial(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    update_group: GroupUpdatePartial,
    group: Annotated[Group, Depends(group_by_id)]
) -> Group:
    return await groups_crud.update_group(
        session=session,
        update_group=update_group,
        group=group,
        partial=True
    )


@router.delete("/{entity_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_group(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    group: Annotated[Group, Depends(group_by_id)]
) -> None:
    return await groups_crud.delete_group(
        session=session, 
        group=group
    )