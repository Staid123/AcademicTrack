from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from ..utils.enums import WeekType
from .base import Base


if TYPE_CHECKING:
    from .group import Group
    from .daily_schedule import DailySchedule


class WeeklySchedule(Base):
    week_type: Mapped[WeekType] # знам/чис
    group_id: Mapped[int] = mapped_column(ForeignKey('group.id'), unique=True) 
    group: Mapped["Group"] = relationship('Group', back_populates='weekly_schedule') 
    daily_schedules: Mapped[list["DailySchedule"]] = relationship('DailySchedule', back_populates='weekly_schedule')