from pydantic import BaseModel, ConfigDict

from core.utils.enums import SemesterNumber


class SemesterBase(BaseModel):
    year: int
    number: SemesterNumber


class SemesterCreate(SemesterBase):
    pass


class SemesterUpdate(SemesterCreate):
    pass


class SemesterUpdatePartial(SemesterCreate):
    year: int | None = None
    number: SemesterNumber | None = None


class Semester(SemesterBase):
    model_config = ConfigDict(from_attributes=True)

    id: int