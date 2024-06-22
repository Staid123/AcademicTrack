from sqlalchemy.orm import Mapped, relationship
from typing import TYPE_CHECKING
from .base import Base
from .enums import UserStatus


if TYPE_CHECKING:
    from .subject import Subject


class Teacher(Base):
    lastname: Mapped[str]
    firstname: Mapped[str]
    patronymic: Mapped[str]
    password: Mapped[str]
    email: Mapped[str]
    status: Mapped["UserStatus"]
    subjects: Mapped[list["Subject"]] = relationship("Subject", back_populates="teacher")