from core.schemas import TeacherRead, SubjectRead
from core.schemas import LessonRead


class Teacher(TeacherRead):
    subjects: list[SubjectRead]


class Subject(SubjectRead):
    teacher: TeacherRead
    lessons: list[LessonRead]