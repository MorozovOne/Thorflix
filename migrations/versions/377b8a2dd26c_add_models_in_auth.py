"""Add models in auth

Revision ID: 377b8a2dd26c
Revises: 65cc790442b0
Create Date: 2023-12-07 01:45:29.744062

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '377b8a2dd26c'
down_revision: Union[str, None] = '65cc790442b0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
