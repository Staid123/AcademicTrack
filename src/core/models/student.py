from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from .base import Base
from core.utils.user_mixin import UserMixin


if TYPE_CHECKING:
    from .group import Group
    from .associations import StudentSubjectAssociation



class Student(Base, UserMixin):
    registration_number: Mapped[int]
    budget: Mapped[bool]
    group_id: Mapped[int] = mapped_column(ForeignKey('group.id'))
    group: Mapped["Group"] = relationship("Group", back_populates="students")
    subjects_details: Mapped[list["StudentSubjectAssociation"]] = relationship('StudentSubjectAssociation', back_populates='student')