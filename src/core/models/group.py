from sqlalchemy import CheckConstraint, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from .base import Base


if TYPE_CHECKING:
    from .student import Student
    from .weekly_schedule import WeeklySchedule


class Group(Base):
    course: Mapped[int]
    number: Mapped[int] = mapped_column(unique=True) # 911
    faculty: Mapped[str] # факультет
    chair: Mapped[str] # кафедра
    specialty: Mapped[str] # спеціальність
    specialty_code: Mapped[int] # код спеціальності
    curator: Mapped[int] = mapped_column(ForeignKey("teacher.id"), unique=True)
    students: Mapped[list["Student"]] = relationship("Student", back_populates="group")
    weekly_schedule: Mapped["WeeklySchedule"] = relationship('WeeklySchedule', uselist=False, back_populates='group')

    __table_args__ = (
        CheckConstraint('course >= 1 AND course <= 5', name='check_course_range'),
    )