from pydantic import BaseModel

from core.utils.enums import UserStatus


class StudentBase(BaseModel):
    lastname: str
    firstname: str
    patronymic: str
    password: str
    email: str
    status: UserStatus
    registration_number: int
    budget: bool
    group_id: int