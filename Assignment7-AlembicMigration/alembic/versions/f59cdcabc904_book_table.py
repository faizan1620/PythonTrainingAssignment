"""book table

Revision ID: f59cdcabc904
Revises: fc87c6b54d0f
Create Date: 2023-04-13 23:01:12.619949

"""
from sqlalchemy import INTEGER, VARCHAR, Column, ForeignKey
from alembic import op

# revision identifiers, used by Alembic.
revision = 'f59cdcabc904'
down_revision = 'fc87c6b54d0f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
    'book',
    Column('id', INTEGER, primary_key=True),
    Column('title', VARCHAR(50), nullable=False),
    Column('department', VARCHAR(50)),
    Column('book_id',INTEGER, ForeignKey('student.id')),
)


def downgrade() -> None:
    op.drop_table('book')
