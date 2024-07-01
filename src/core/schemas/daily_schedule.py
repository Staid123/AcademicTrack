from pydantic import BaseModel, ConfigDict

from core.schemas import LessonRead
from core.utils.enums import Day


class DailyScheduleBase(BaseModel):
    day: Day
    weekly_schedule_id: int


class DailyScheduleCreate(DailyScheduleBase):
    day: Day
    weekly_schedule_id: int


class DailyScheduleRead(DailyScheduleCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)


class DailySchedule(DailyScheduleRead):
    # weekly_schedule: WeeklySchedule
    lessons: list[LessonRead]


class DailyScheduleUpdate(DailyScheduleCreate):
    pass


class DailyScheduleUpdatePartial(BaseModel):
    day: Day | None = None
    weekly_schedule_id: int | None = None