from pydantic import BaseModel, ConfigDict


# from core.models.daily_schedule import DailySchedule
from core.utils.enums import LessonType
from core.schemas import SubjectRead


class LessonBase(BaseModel):
    daily_schedule_id: int
    number: int
    lesson_type: LessonType
    subject_id: int
    


class LessonCreate(LessonBase):
    pass


class LessonRead(LessonCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
    


class Lesson(LessonRead):
    # daily_schedule: DailySchedule
    subject: SubjectRead


class LessonUpdate(LessonCreate):
    pass


class LessonUpdatePartial(BaseModel):
    number: int | None = None
    lesson_type: LessonType | None = None
    subject_id: int | None = None
    daily_schedule_id: int | None = None