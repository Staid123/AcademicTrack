from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from .base import Base
from .enums import UserStatus


if TYPE_CHECKING:
    from .group import Group
    from .associations import StudentSubjectAssociation



class Student(Base):
    lastname: Mapped[str]
    firstname: Mapped[str]
    patronymic: Mapped[str]
    registration_number: Mapped[int]
    password: Mapped[str]
    email: Mapped[str]
    budget: Mapped[bool]
    status: Mapped["UserStatus"]
    group_id: Mapped[int] = mapped_column(ForeignKey('group.id'))
    group: Mapped["Group"] = relationship("Group", back_populates="students")
    subjects_details: Mapped[list["StudentSubjectAssociation"]] = relationship('StudentSubjectAssociation', back_populates='student')

    __table_args__ = (
         UniqueConstraint("lastname", "firstname", "patronymic"),
    )