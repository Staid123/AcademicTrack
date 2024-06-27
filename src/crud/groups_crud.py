from typing import Sequence
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Group
from core.schemas import GroupCreate, GroupUpdate, GroupUpdatePartial


async def get_groups_with_students(
    session: AsyncSession,
    skip: int,
    limit: int
) -> Sequence[Group]:
    stmt = select(Group).options(selectinload(Group.students)).offset(skip).limit(limit).order_by(Group.id)
    result = await session.scalars(stmt)
    return result.all()


async def get_group(
    session: AsyncSession,
    entity_id: int
) -> Group:
    stmt = select(Group).options(selectinload(Group.students)).where(Group.id==entity_id)
    group = await session.scalars(stmt)
    return group.one_or_none()


async def create_group(
    session: AsyncSession,
    group_in: GroupCreate        
) -> Group:
    group = Group(**group_in.model_dump())
    session.add(group)
    await session.commit()
    return group



async def update_group(
    session: AsyncSession,
    update_group: GroupUpdate,
    group: Group,
    partial: bool = False
) -> Group:
    for name, value in update_group.model_dump(exclude_unset=partial).items():
        setattr(group, name, value)
    await session.commit()
    return group


async def delete_group(
    session: AsyncSession,
    group: Group
) -> None:
    await session.delete(group)
    await session.commit()
