"""Add comments folder

Revision ID: 8a20956eebe8
Revises: 07fcfb310ddc
Create Date: 2023-12-07 02:06:09.995593

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8a20956eebe8'
down_revision: Union[str, None] = '07fcfb310ddc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
