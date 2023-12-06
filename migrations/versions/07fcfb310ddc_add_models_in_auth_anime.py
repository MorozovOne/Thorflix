"""Add models in auth/anime

Revision ID: 07fcfb310ddc
Revises: 377b8a2dd26c
Create Date: 2023-12-07 01:51:10.591338

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '07fcfb310ddc'
down_revision: Union[str, None] = '377b8a2dd26c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
