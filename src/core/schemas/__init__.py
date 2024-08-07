__all__ = (
    "SemesterCreate", "Semester", "SemesterUpdate", "SemesterUpdatePartial",
    "Student", "StudentWithGroup", "StudentCreate", "StudentUpdate", "StudentUpdatePartial",
    "Group", "GroupWithStudents", "GroupCreate", "GroupUpdate", "GroupUpdatePartial",
    "TeacherRead", "TeacherCreate", "TeacherUpdate", "TeacherUpdatePartial", "Teacher",
    "Subject", "SubjectCreate", "SubjectUpdate", "SubjectUpdatePartial", "SubjectRead", "SubjectOnlyWithTeacher",
    "Lesson", "LessonCreate", "LessonRead", "LessonUpdate", "LessonUpdatePartial",
    "DailySchedule", "DailyScheduleCreate", "DailyScheduleRead", "DailyScheduleUpdate", "DailyScheduleUpdatePartial",
    "WeeklySchedule", "WeeklyScheduleCreate", "WeeklyScheduleRead", "WeeklyScheduleUpdate", "WeeklyScheduleUpdatePartial",
    "Grade", "GradeCreate", "GradeUpdate", "GradeUpdatePartial", "GradeRead"
)


from .semester import SemesterCreate, Semester, SemesterUpdate, SemesterUpdatePartial
from .student import Student, StudentCreate, StudentUpdate, StudentUpdatePartial
from .group import Group, GroupCreate, GroupUpdate, GroupUpdatePartial
from .teacher import TeacherRead, TeacherCreate, TeacherUpdate, TeacherUpdatePartial
from .student_group import GroupWithStudents, StudentWithGroup
from .subject import SubjectCreate, SubjectUpdate, SubjectUpdatePartial, SubjectRead
from .lesson import Lesson, LessonCreate, LessonRead, LessonUpdate, LessonUpdatePartial
from .subject_teacher import Subject, Teacher, SubjectOnlyWithTeacher
from .daily_schedule import DailySchedule, DailyScheduleCreate, DailyScheduleRead, DailyScheduleUpdate, DailyScheduleUpdatePartial
from .weekly_schedule import WeeklySchedule, WeeklyScheduleCreate, WeeklyScheduleRead, WeeklyScheduleUpdate, WeeklyScheduleUpdatePartial
from .grades import Grade, GradeCreate, GradeUpdate, GradeUpdatePartial, GradeRead