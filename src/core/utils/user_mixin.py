from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped
from .enums import UserStatus


class UserMixin:
    lastname: Mapped[str]
    firstname: Mapped[str]
    patronymic: Mapped[str]
    password: Mapped[str]
    email: Mapped[str]
    status: Mapped["UserStatus"]

    __table_args__ = (
         UniqueConstraint("lastname", "firstname", "patronymic"),
    )