"""add cols to events

Revision ID: 5b1792f6f3cf
Revises: 68e00a8c650e
Create Date: 2025-11-16 15:11:02.731711

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5b1792f6f3cf'
down_revision: Union[str, Sequence[str], None] = '68e00a8c650e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('events', sa.Column('date', sa.DATE, nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('events', 'date')
