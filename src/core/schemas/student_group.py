
from core.schemas.group import Group
from core.schemas.student import Student


class GroupWithStudents(Group):
    students: list[Student]


class StudentWithGroup(Student):
    group: Group