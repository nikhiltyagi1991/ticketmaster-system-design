"""create all entities

Revision ID: 68e00a8c650e
Revises: 0c3bac4dd7a4
Create Date: 2025-11-16 09:46:21.176776

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '68e00a8c650e'
down_revision: Union[str, Sequence[str], None] = '0c3bac4dd7a4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
        sa.Column('name', sa.String(500), nullable=False),
        sa.Column('emailid', sa.String(500), nullable=False, unique=True),
        sa.Column('password', sa.String(512), nullable=False),
        sa.Column('dob', sa.DATE(), nullable=True)
    )
    op.create_table(
        'performer',
        sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
        sa.Column('name', sa.String(500), nullable=False),
        sa.Column('bio', sa.String(10000), nullable=False),
        sa.Column('type', sa.String(300), nullable=True),
        sa.Column('photo_url', sa.String(300), nullable=True),
    )
    op.create_table(
        'venue',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(500), nullable=False),
        sa.Column('about', sa.String(10000), nullable=True),
        sa.Column('notes', sa.String(10000), nullable=True),
        sa.Column('city', sa.String(100), nullable=False),
        sa.Column('country', sa.String(100), nullable=False),
        sa.Column('lat', sa.String(100), nullable=True),
        sa.Column('lon', sa.String(100), nullable=True),
        sa.Column('seatchart_id', sa.Integer, sa.ForeignKey('seatchart.id'), nullable=True)
    )
    op.rename_table('seatchart', 'spacechart')
    op.add_column(
        'spacechart',
        sa.Column('venue_id', sa.Integer, sa.ForeignKey('venue.id'), nullable=False)
    )
    op.create_table(
        'space',
        sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
        sa.Column('venue_id', sa.Integer, sa.ForeignKey('venue.id')),
        sa.Column('type', sa.String(400), nullable=True)
    )
    op.create_table(
        'events',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(500), nullable=False),
        sa.Column('description', sa.String(10000), nullable=False),
        sa.Column('type', sa.String(100), nullable=False),
        sa.Column('venue_id', sa.Integer, sa.ForeignKey('venue.id'), nullable=False)
    )
    op.create_table(
        'tickets',
        sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
        sa.Column('status', sa.String(500), nullable=False), # Booked/Available/Reserved
        sa.Column('event_id', sa.Integer, sa.ForeignKey('events.id'), nullable=False),
        sa.Column('space_id', sa.Integer, sa.ForeignKey('space.id'), nullable=True)
    )
    op.create_table(
        'booking',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('ticket_id', sa.Integer, sa.ForeignKey('tickets.id'), nullable=False),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('user.id'), nullable=False)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('user')
    op.drop_table('performer')
    op.drop_table('venue')
    op.drop_table('space')
    op.drop_table('tickets')
    op.drop_table('events')
    op.drop_table('booking')
    op.rename_table('spacechart','seatchart')
