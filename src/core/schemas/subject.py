from datetime import datetime
from pydantic import BaseModel, ConfigDict

from core.schemas import TeacherRead



class SubjectBase(BaseModel):
    name: str
    teacher_id: int
    exam_date: datetime | None = None


class SubjectCreate(SubjectBase):
    pass


class SubjectUpdate(SubjectCreate):
    pass


class SubjectUpdatePartial(BaseModel):
    name: str | None = None
    teacher_id: int | None = None
    exam_date: datetime | None = None


class SubjectRead(SubjectCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
