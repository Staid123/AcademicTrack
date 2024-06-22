from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from .base import Base
from .enums import LessonType


if TYPE_CHECKING:
    from .subject import Subject
    from .daily_schedule import DailySchedule



class Lesson(Base):
    daily_schedule_id: Mapped[int] = mapped_column(ForeignKey('daily_schedule.id'))
    daily_schedule: Mapped["DailySchedule"] = relationship('DailySchedule', back_populates='lessons')
    number: Mapped[int]
    lesson_type: Mapped[LessonType] # лекция/лаба/практическая/консультация/єкзамен
    subject_id: Mapped[int] = mapped_column(ForeignKey('subject.id'))
    subject: Mapped["Subject"] = relationship("Group", back_populates="students")