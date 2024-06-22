from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship
from typing import TYPE_CHECKING
from .base import Base
from .enums import Day


if TYPE_CHECKING:
    from .weekly_schedule import WeeklySchedule


class DailySchedule(Base):
    day: Mapped["Day"]
    weekly_schedule_id: Mapped[int] = ForeignKey('weekly_schedules.id')
    weekly_schedule: Mapped["WeeklySchedule"] = relationship('WeeklySchedule', back_populates='daily_schedule')
    lessons = relationship('Lesson', back_populates='daily_schedule')