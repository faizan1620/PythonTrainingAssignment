"""student table

Revision ID: fc87c6b54d0f
Revises:
Create Date: 2023-03-31 22:39:32.265803

"""
from sqlalchemy import INTEGER, VARCHAR, Column
from alembic import op


# revision identifiers, used by Alembic.
revision = "fc87c6b54d0f"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "student",
        Column("id", INTEGER, primary_key=True),
        Column("name", VARCHAR(50), nullable=False),
        Column("branch", VARCHAR(50)),
        Column("age", INTEGER),
        Column("gender", VARCHAR(50)),
        Column("registration", INTEGER),
    )


def downgrade() -> None:
    op.drop_table("student")
