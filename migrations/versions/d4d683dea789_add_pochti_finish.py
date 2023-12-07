"""Add Pochti Finish

Revision ID: d4d683dea789
Revises: 6de9861596e5
Create Date: 2023-12-08 01:20:09.174566

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd4d683dea789'
down_revision: Union[str, None] = '6de9861596e5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
