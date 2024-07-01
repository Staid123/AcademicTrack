"""empty message

Revision ID: 719926efd85d
Revises: bd45bd2a8ea7
Create Date: 2024-06-28 19:50:34.820806

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "719926efd85d"
down_revision: Union[str, None] = "bd45bd2a8ea7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "weekly_schedule",
        sa.Column("semester_id", sa.Integer(), nullable=False),
    )
    op.drop_constraint(
        "uq_weekly_schedule_group_id", "weekly_schedule", type_="unique"
    )
    op.create_unique_constraint(
        op.f("uq_weekly_schedule_week_type_group_id_semester_id"),
        "weekly_schedule",
        ["week_type", "group_id", "semester_id"],
    )
    op.create_foreign_key(
        op.f("fk_weekly_schedule_semester_id_semester"),
        "weekly_schedule",
        "semester",
        ["semester_id"],
        ["id"],
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        op.f("fk_weekly_schedule_semester_id_semester"),
        "weekly_schedule",
        type_="foreignkey",
    )
    op.drop_constraint(
        op.f("uq_weekly_schedule_week_type_group_id_semester_id"),
        "weekly_schedule",
        type_="unique",
    )
    op.create_unique_constraint(
        "uq_weekly_schedule_group_id", "weekly_schedule", ["group_id"]
    )
    op.drop_column("weekly_schedule", "semester_id")

    # ### end Alembic commands ###
