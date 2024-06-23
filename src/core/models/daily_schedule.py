from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column
from typing import TYPE_CHECKING
from .base import Base
from ..utils.enums import Day


if TYPE_CHECKING:
    from .weekly_schedule import WeeklySchedule


class DailySchedule(Base):
    day: Mapped["Day"]
    weekly_schedule_id: Mapped[int] = mapped_column(ForeignKey('weekly_schedule.id'))
    weekly_schedule: Mapped["WeeklySchedule"] = relationship('WeeklySchedule', back_populates='daily_schedules')
    lessons = relationship('Lesson', back_populates='daily_schedule')