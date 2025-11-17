"""create seatchart table

Revision ID: 0c3bac4dd7a4
Revises: 
Create Date: 2025-11-15 20:06:28.242932

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0c3bac4dd7a4'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "seatchart",
        sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
        sa.Column('file_url', sa.String(100), nullable=True),
        sa.Column('metadata', sa.String(1000), nullable=True)
    )
    


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('seatchart')
