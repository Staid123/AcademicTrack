from sqlalchemy import select
from sqlalchemy.orm import selectinload, joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import WeeklySchedule
from core.models import DailySchedule, Lesson
from core.schemas import WeeklyScheduleUpdate, WeeklyScheduleUpdatePartial, WeeklyScheduleCreate, WeeklyScheduleRead


async def get_all_weekly_schedules_with_daily_schedules_and_group_and_semester(
    session: AsyncSession,
    skip: int,
    limit: int
) -> list[WeeklySchedule]:
    stmt = (
        select(WeeklySchedule).options(
            selectinload(WeeklySchedule.daily_schedules).selectinload(DailySchedule.lessons).joinedload(Lesson.subject),
            joinedload(WeeklySchedule.semester),
            joinedload(WeeklySchedule.group)
        )
        .offset(skip)
        .limit(limit)
        .order_by(WeeklySchedule.id)
    )
    weekly_schedules = await session.scalars(stmt)
    return weekly_schedules.all()


async def get_weekly_schedule(
    session: AsyncSession,
    entity_id: int
) -> WeeklySchedule:
    stmt = (
        select(WeeklySchedule).options(
            selectinload(WeeklySchedule.daily_schedules).selectinload(DailySchedule.lessons).joinedload(Lesson.subject),
            joinedload(WeeklySchedule.semester),
            joinedload(WeeklySchedule.group)
        )
        .where(WeeklySchedule.id==entity_id)
    )
    weekly_schedule = await session.scalars(stmt)
    return weekly_schedule.one_or_none()


async def create_weekly_schedule(
    session: AsyncSession,
    weekly_schedule_in: WeeklyScheduleCreate
) -> WeeklyScheduleRead:
    weekly_schedule = WeeklySchedule(**weekly_schedule_in.model_dump())
    session.add(weekly_schedule)
    await session.commit()
    return weekly_schedule


async def update_weekly_schedule(
    session: AsyncSession,
    weekly_schedule_update: WeeklyScheduleUpdate | WeeklyScheduleUpdatePartial,
    weekly_schedule: WeeklySchedule,
    partial: bool = False
) -> WeeklySchedule:
    for name, value in weekly_schedule_update.model_dump(exclude_unset=partial).items():
        setattr(weekly_schedule, name, value)
    await session.commit()
    return weekly_schedule



async def delete_weekly_schedule(
    session: AsyncSession,
    weekly_schedule: WeeklySchedule
) -> None:
    await session.delete(weekly_schedule)
    await session.commit()