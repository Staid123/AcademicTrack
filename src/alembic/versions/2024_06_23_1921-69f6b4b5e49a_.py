"""empty message

Revision ID: 69f6b4b5e49a
Revises: d73629aa45e6
Create Date: 2024-06-23 19:21:44.093734

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "69f6b4b5e49a"
down_revision: Union[str, None] = "d73629aa45e6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "student_subject_association",
        sa.Column("student_id", sa.Integer(), nullable=True),
    )
    op.add_column(
        "student_subject_association",
        sa.Column("subject_id", sa.Integer(), nullable=True),
    )
    op.create_foreign_key(
        op.f("fk_student_subject_association_student_id_student"),
        "student_subject_association",
        "student",
        ["student_id"],
        ["id"],
    )
    op.create_foreign_key(
        op.f("fk_student_subject_association_subject_id_subject"),
        "student_subject_association",
        "subject",
        ["subject_id"],
        ["id"],
    )
    op.drop_constraint(
        "uq_teacher_lastname_firstname_patronymic", "teacher", type_="unique"
    )
    op.create_unique_constraint(
        op.f("uq_teacher_lastname_firstname_patronymic"),
        "teacher",
        ["lastname", "firstname", "patronymic"],
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        op.f("uq_teacher_lastname_firstname_patronymic"),
        "teacher",
        type_="unique",
    )
    op.create_unique_constraint(
        "uq_teacher_lastname_firstname_patronymic",
        "teacher",
        ["lastname", "firstname", "patronymic"],
    )
    op.drop_constraint(
        op.f("fk_student_subject_association_subject_id_subject"),
        "student_subject_association",
        type_="foreignkey",
    )
    op.drop_constraint(
        op.f("fk_student_subject_association_student_id_student"),
        "student_subject_association",
        type_="foreignkey",
    )
    op.drop_column("student_subject_association", "subject_id")
    op.drop_column("student_subject_association", "student_id")
    # ### end Alembic commands ###
