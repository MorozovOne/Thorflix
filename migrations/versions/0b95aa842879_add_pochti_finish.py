"""Add Pochti Finish

Revision ID: 0b95aa842879
Revises: d4d683dea789
Create Date: 2023-12-08 01:21:17.829492

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0b95aa842879'
down_revision: Union[str, None] = 'd4d683dea789'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
