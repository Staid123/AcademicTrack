from sqlalchemy.orm import Mapped, relationship
from typing import TYPE_CHECKING
from .base import Base
from core.utils.user_mixin import UserMixin


if TYPE_CHECKING:
    from .subject import Subject


class Teacher(Base, UserMixin):
    subjects: Mapped[list["Subject"]] = relationship("Subject", back_populates="teacher")