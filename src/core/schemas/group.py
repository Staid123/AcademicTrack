from pydantic import BaseModel, ConfigDict


class GroupBase(BaseModel):
    course: int
    number: int
    faculty: str
    chair: str
    specialty: str
    specialty_code: int
    curator_id: int
    

class Group(GroupBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class GroupCreate(GroupBase):
    pass


class GroupUpdate(GroupCreate):
    pass


class GroupUpdatePartial(BaseModel):
    course: int | None = None
    number: int | None = None
    faculty: str | None = None
    chair: str | None = None
    specialty: str | None = None
    specialty_code: int | None = None
    curator_id: int | None = None