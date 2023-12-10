"""Pochti Finish

Revision ID: fc0a160ddbc3
Revises: 
Create Date: 2023-12-10 17:03:59.847365

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'fc0a160ddbc3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('anime')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('anime',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('poster', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('type', postgresql.ENUM('TV', name='type'), autoincrement=False, nullable=True),
    sa.Column('genre', postgresql.ENUM('Comedia', name='genre'), autoincrement=False, nullable=True),
    sa.Column('episodes', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('duration', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='anime_pkey')
    )
    # ### end Alembic commands ###