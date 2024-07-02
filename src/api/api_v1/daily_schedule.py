from typing import Annotated
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from core import db_helper
from core.schemas import DailyScheduleRead, DailyScheduleCreate, DailyScheduleUpdate, DailyScheduleUpdatePartial, DailySchedule
from crud import daily_schedules_crud
from dependencies import daily_schedule_by_id


router = APIRouter(prefix="/daily_schedule", tags=["Daily Schedule"])


@router.get("/", response_model=list[DailySchedule])
async def get_all_daily_schedules_with_lessons_and_subject(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    skip: int = Query(0, ge=0), 
    limit: int = Query(10, ge=1),
) -> list[DailySchedule]:
    return await daily_schedules_crud.get_all_daily_schedules_with_lessons(
        session=session,
        skip=skip,
        limit=limit
    )


@router.get("/{entity_id}/", response_model=DailySchedule)
async def get_daily_schedule_with_lessons_and_subject(
    daily_schedule: Annotated[DailySchedule, Depends(daily_schedule_by_id)]
) -> DailySchedule:
    return daily_schedule


@router.post("/", response_model=DailyScheduleRead, status_code=status.HTTP_201_CREATED)
async def create_daily_schedule(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    daily_schedule_in: DailyScheduleCreate
) -> DailyScheduleRead:
    return await daily_schedules_crud.create_daily_schedule(
        session=session,
        daily_schedule_in=daily_schedule_in
    )


@router.put("/{entity_id}/", response_model=DailySchedule)
async def update_daily_schedule(
    daily_schedule: Annotated[DailySchedule, Depends(daily_schedule_by_id)],
    daily_schedule_update: DailyScheduleUpdate,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
) -> DailySchedule:
    return await daily_schedules_crud.update_daily_schedule(
        session=session,
        daily_schedule=daily_schedule,
        daily_schedule_update=daily_schedule_update
    )


@router.patch("/{entity_id}/", response_model=DailySchedule)
async def update_daily_schedule_partial(
    daily_schedule: Annotated[DailySchedule, Depends(daily_schedule_by_id)],
    daily_schedule_update: DailyScheduleUpdatePartial,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
) -> DailySchedule:
    return await daily_schedules_crud.update_daily_schedule(
        session=session,
        daily_schedule=daily_schedule,
        daily_schedule_update=daily_schedule_update,
        partial=True
    )


@router.delete("/{entity_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_daily_schedule(
    daily_schedule: Annotated[DailySchedule, Depends(daily_schedule_by_id)],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
) -> None:
    return await daily_schedules_crud.delete_daily_schedule(
        session=session,
        daily_schedule=daily_schedule
    )