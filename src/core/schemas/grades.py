from pydantic import BaseModel, ConfigDict

from core.schemas import Student, SubjectOnlyWithTeacher, Semester


class GradeBase(BaseModel):
    student_id: int
    subject_id: int
    kz1: int = 0
    kz2: int = 0
    exam_grade: int = 0
    semester_id: int


class GradeCreate(GradeBase):
    pass


class GradeUpdate(GradeCreate):
    pass


class GradeUpdatePartial(BaseModel):
    student_id: int | None = None
    subject_id: int | None = None
    kz1: int = 0
    kz2: int = 0
    exam_grade: int = 0
    semester_id: int | None = None


class GradeRead(GradeBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class Grade(GradeRead):
    student: Student
    subject: SubjectOnlyWithTeacher
    semester: Semester
    