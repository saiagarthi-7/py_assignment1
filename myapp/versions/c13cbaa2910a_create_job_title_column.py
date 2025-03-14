"""create job_title column

Revision ID: c13cbaa2910a
Revises: 14ce592ed8de
Create Date: 2025-03-13 09:56:56.630570

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c13cbaa2910a'
down_revision: Union[str, None] = '14ce592ed8de'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('user',sa.Column('job_title',sa.String,nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('user','job_title')
