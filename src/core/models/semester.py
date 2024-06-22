from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from .base import Base
from .enums import SemesterNumber


if TYPE_CHECKING:
    from .associations import StudentSubjectAssociation


class Semester(Base):
    year: Mapped[int]
    number: Mapped["SemesterNumber"]
    grades: Mapped[list["StudentSubjectAssociation"]] = relationship("StudentSubjectAssociation", back_populates="semester") 