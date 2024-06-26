from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from .base import Base
from ..utils.enums import SemesterNumber


if TYPE_CHECKING:
    from .associations import StudentSubjectAssociation
    from .weekly_schedule import WeeklySchedule


class Semester(Base):
    year: Mapped[int]
    number: Mapped["SemesterNumber"]
    grades: Mapped[list["StudentSubjectAssociation"]] = relationship("StudentSubjectAssociation", back_populates="semester") 
    weekly_schedules: Mapped[list["WeeklySchedule"]] = relationship("WeeklySchedule", back_populates="semester")

    __table_args__ = (
        UniqueConstraint("year", "number"), 
    )