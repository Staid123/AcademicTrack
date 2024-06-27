from pydantic import BaseModel, ConfigDict

from core.utils.enums import UserStatus


class StudentGroup(BaseModel):
    id: int
    course: int
    number: int
    faculty: str
    chair: str
    specialty: str
    specialty_code: int
    curator_id: int


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


class Student(StudentBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int


class StudentWithGroup(Student):
    group: StudentGroup 


class StudentCreate(StudentBase):
    pass


class StudentUpdate(StudentCreate):
    pass


class StudentUpdatePartial(StudentCreate):
    lastname: str | None = None
    firstname: str | None = None
    patronymic: str | None = None
    password: str | None = None
    email: str | None = None
    status: UserStatus | None = None
    registration_number: int | None = None
    budget: bool | None = None
    group_id: int | None = None