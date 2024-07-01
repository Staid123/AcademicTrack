"""add uniqueconstraint for studentsubjectassociation

Revision ID: bd45bd2a8ea7
Revises: 6d0454cbc2c0
Create Date: 2024-06-28 17:46:01.493775

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "bd45bd2a8ea7"
down_revision: Union[str, None] = "6d0454cbc2c0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(
        op.f(
            "uq_student_subject_association_semester_id_student_id_subject_id"
        ),
        "student_subject_association",
        ["semester_id", "student_id", "subject_id"],
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        op.f(
            "uq_student_subject_association_semester_id_student_id_subject_id"
        ),
        "student_subject_association",
        type_="unique",
    )
    # ### end Alembic commands ###
