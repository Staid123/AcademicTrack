from sqlalchemy import CheckConstraint, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from .base import Base


if TYPE_CHECKING:
    from .subject import Subject
    from .student import Student
    from .semester import Semester


class StudentSubjectAssociation(Base):
    student: Mapped["Student"] = relationship(back_populates='subjects_details')
    subject: Mapped["Subject"] = relationship(back_populates='students_details')
    student_id = mapped_column(ForeignKey('student.id'))
    subject_id = mapped_column(ForeignKey('subject.id'))
    kz1: Mapped[int | None] = mapped_column(default=0, server_default="0")
    kz2: Mapped[int | None] = mapped_column(default=0, server_default="0")
    exam_grade: Mapped[int | None] = mapped_column(default=0, server_default="0")
    semester: Mapped["Semester"] = relationship('Semester', back_populates='grades')
    semester_id: Mapped[int] = mapped_column(ForeignKey('semester.id'))

    __table_args__ = (
        CheckConstraint('kz1 >= 0 AND kz1 <= 100', name='check_kz1_range'),
        CheckConstraint('kz2 >= 0 AND kz2 <= 100', name='check_kz2_range'),
        UniqueConstraint("semester_id", "student_id", "subject_id")
    )