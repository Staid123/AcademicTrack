from core.schemas import TeacherRead, SubjectRead
from core.schemas import LessonRead


class Teacher(TeacherRead):
    subjects: list[SubjectRead]


class SubjectOnlyWithTeacher(SubjectRead):
    teacher: TeacherRead

class Subject(SubjectOnlyWithTeacher):
    lessons: list[LessonRead]


