from pydantic import BaseModel

from core.utils.enums import SemesterNumber


class SemesterBase(BaseModel):
    year: int
    number: SemesterNumber


class SemesterRead(SemesterBase):
    id: int


class SemesterCreate(SemesterBase):
    pass