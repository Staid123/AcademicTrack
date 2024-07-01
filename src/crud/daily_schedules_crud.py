from typing import Sequence
from sqlalchemy import select
from sqlalchemy.orm import selectinload, joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import DailySchedule
from core.schemas import DailyScheduleUpdate, DailyScheduleUpdatePartial, DailyScheduleCreate, DailyScheduleRead


async def get_all_daily_schedules_with_lessons(
    session: AsyncSession,
    limit: int,
    skip: int
) -> list[DailySchedule]:
    stmt = (
        select(DailySchedule)
        .options(selectinload(DailySchedule.lessons))
        .offset(skip)
        .limit(limit)
        .order_by(DailySchedule.id)
    )
    daily_schedules = await session.scalars(stmt)
    return daily_schedules.all()


async def get_daily_schedule(
    session: AsyncSession,
    entity_id: int
) -> DailySchedule:
    stmt = (
        select(DailySchedule)
        .options(selectinload(DailySchedule.lessons))
        .where(DailySchedule.id==entity_id)
    )
    daily_schedule = await session.scalars(stmt)
    return daily_schedule.one_or_none()


async def create_daily_schedule(
    session: AsyncSession,
    daily_schedule_in: DailyScheduleCreate
) -> DailyScheduleRead:
    daily_schedule = DailySchedule(**daily_schedule_in.model_dump())
    session.add(daily_schedule)
    await session.commit()
    return daily_schedule


async def update_daily_schedule(
    session: AsyncSession,
    daily_schedule: DailySchedule,
    daily_schedule_update: DailyScheduleUpdate | DailyScheduleUpdatePartial,
    partial: bool = False
) -> DailySchedule:
    for name, value in daily_schedule_update.model_dump(exclude_unset=partial).items():
        setattr(daily_schedule, name, value)
    await session.commit()
    return daily_schedule


async def delete_daily_schedule(
    session: AsyncSession,
    daily_schedule: DailySchedule
) -> None:
    await session.delete(daily_schedule)
    await session.commit()