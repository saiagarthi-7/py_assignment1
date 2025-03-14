"""Create User table

Revision ID: 14ce592ed8de
Revises: 
Create Date: 2025-03-13 09:35:59.257394

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '14ce592ed8de'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'user',
        sa.Column('id',sa.Integer,primary_key=True),
        sa.Column('name',sa.String,nullable=False),
        sa.Column('current_status',sa.Boolean,default=True)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('user')
