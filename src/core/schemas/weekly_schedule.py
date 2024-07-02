from pydantic import BaseModel, ConfigDict

from core.schemas import Semester, DailySchedule, Group
from core.utils.enums import WeekType


class WeeklyScheduleBase(BaseModel):
    week_type: WeekType
    group_id: int
    semester_id: int


class WeeklyScheduleCreate(WeeklyScheduleBase):
    pass


class WeeklyScheduleRead(WeeklyScheduleBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class WeeklySchedule(WeeklyScheduleRead):
    group: Group
    daily_schedules: list[DailySchedule]
    semester: Semester    
    

class WeeklyScheduleUpdate(WeeklyScheduleCreate):
    pass


class WeeklyScheduleUpdatePartial(BaseModel):
    week_type: WeekType | None = None
    group_id: int | None = None
    semester_id: int | None = None