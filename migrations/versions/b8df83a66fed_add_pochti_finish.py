"""Add Pochti Finish

Revision ID: b8df83a66fed
Revises: 0b95aa842879
Create Date: 2023-12-08 01:28:00.454404

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b8df83a66fed'
down_revision: Union[str, None] = '0b95aa842879'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
