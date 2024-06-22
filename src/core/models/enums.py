import enum


class UserStatus(enum.Enum):
    active: str = "active"
    inactive: str = "inactive"


class SemesterNumber(enum.Enum):
    first = 1
    second = 2


class LessonType(enum.Enum):
    lecture = "лекция"
    laboratory = "лабораторная"
    practical = "практическая"
    consultation = "консультация"
    exam = "экзамен"


class WeekType(enum.Enum):
    denominator = "знаменатель"
    numerator = "числитель"


class Day(enum.Enum):
    monday = "понедельник"
    tuesday = "вторник"
    wednesday = "среда"
    thursday = "четверг"
    friday = "пятница"