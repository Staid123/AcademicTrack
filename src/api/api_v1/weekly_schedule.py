from typing import Annotated
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from core import db_helper
from core.schemas import WeeklyScheduleRead, WeeklyScheduleCreate, WeeklyScheduleUpdate, WeeklyScheduleUpdatePartial, WeeklySchedule
from crud import weekly_schedules_crud
from dependencies import weekly_schedule_by_id


router = APIRouter(prefix="/weekly_schedule", tags=["Weekly Schedule"])


@router.get("/", response_model=list[WeeklySchedule])
async def get_all_weekly_schedules_with_daily_schedules_and_group_and_semester(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    skip: int = Query(0, ge=0), 
    limit: int = Query(10, ge=1),
) -> list[WeeklySchedule]:
    return await weekly_schedules_crud.get_all_weekly_schedules_with_daily_schedules_and_group_and_semester(
        session=session,
        skip=skip,
        limit=limit
    )


@router.get("/{entity_id}/", response_model=WeeklySchedule)
async def get_weekly_schedule_with_daily_schedules_and_group_and_semester(
    weekly_schedule: Annotated[WeeklySchedule, Depends(weekly_schedule_by_id)]
) -> WeeklySchedule:
    return weekly_schedule


@router.post("/", response_model=WeeklyScheduleRead)
async def create_weekly_schedule(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    weekly_schedule_in: WeeklyScheduleCreate
) -> WeeklyScheduleRead:
    return await weekly_schedules_crud.create_weekly_schedule(
        session=session,
        weekly_schedule_in=weekly_schedule_in
    )


@router.put("/{entity_id}/", response_model=WeeklySchedule)
async def update_weekly_schedule(
    weekly_schedule: Annotated[WeeklySchedule, Depends(weekly_schedule_by_id)],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    weekly_schedule_update: WeeklyScheduleUpdate
) -> WeeklySchedule:
    return await weekly_schedules_crud.update_weekly_schedule(
        session=session,
        weekly_schedule=weekly_schedule,
        weekly_schedule_update=weekly_schedule_update
    )


@router.patch("/{entity_id}/", response_model=WeeklySchedule)
async def update_weekly_schedule_partial(
    weekly_schedule: Annotated[WeeklySchedule, Depends(weekly_schedule_by_id)],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    weekly_schedule_update: WeeklyScheduleUpdatePartial
) -> WeeklySchedule:
    return await weekly_schedules_crud.update_weekly_schedule(
        session=session,
        weekly_schedule=weekly_schedule,
        weekly_schedule_update=weekly_schedule_update,
        partial=True
    )


@router.delete("/{entity_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_weekly_schedule(
    weekly_schedule: Annotated[WeeklySchedule, Depends(weekly_schedule_by_id)],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
) -> None:
    return await weekly_schedules_crud.delete_weekly_schedule(
        session=session,
        weekly_schedule=weekly_schedule
    )