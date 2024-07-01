from pydantic import BaseModel, ConfigDict

from core.utils.enums import UserStatus


class TeacherBase(BaseModel):
    lastname: str
    firstname: str
    patronymic: str
    password: str
    email: str
    status: UserStatus


class TeacherCreate(TeacherBase):
    pass


class TeacherRead(TeacherCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int


class TeacherUpdate(TeacherCreate):
    pass


class TeacherUpdatePartial(BaseModel):
    lastname: str | None = None
    firstname: str | None = None
    patronymic: str | None = None
    password: str | None = None
    email: str | None = None
    status: UserStatus | None = None