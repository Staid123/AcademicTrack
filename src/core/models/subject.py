from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from datetime import datetime
from .base import Base


if TYPE_CHECKING:
    from .teacher import Teacher
    from .lesson import Lesson
    from .associations import StudentSubjectAssociation



class Subject(Base):
    name: Mapped[str]
    teacher_id: Mapped[int] = mapped_column(ForeignKey('teacher.id'))
    teacher: Mapped["Teacher"] = relationship("Teacher", back_populates="subjects")
    lessons: Mapped[list["Lesson"]] = relationship("Lesson", back_populates="subject")
    # Связь многие-ко-многим с Student через таблицу ассоциаций
    # - students = relationship('Student', secondary='student_subject_association', back_populates='subjects')
    students_details: Mapped[list['StudentSubjectAssociation']] = relationship('StudentSubjectAssociation', back_populates='subject')
    exam_date: Mapped[datetime | None]