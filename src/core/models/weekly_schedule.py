from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from ..utils.enums import WeekType
from .base import Base
from sqlalchemy import UniqueConstraint


if TYPE_CHECKING:
    from .group import Group
    from .daily_schedule import DailySchedule
    from .semester import Semester


class WeeklySchedule(Base):
    week_type: Mapped[WeekType] # знам/чис
    group_id: Mapped[int] = mapped_column(ForeignKey('group.id')) 
    group: Mapped["Group"] = relationship('Group', back_populates='weekly_schedules') 
    daily_schedules: Mapped[list["DailySchedule"]] = relationship('DailySchedule', back_populates='weekly_schedule')
    semester: Mapped["Semester"] = relationship('Semester', back_populates="weekly_schedules")
    semester_id: Mapped[int] = mapped_column(ForeignKey('semester.id'))


    __table_args__ = (
        UniqueConstraint("week_type", "group_id", "semester_id"), 
    )