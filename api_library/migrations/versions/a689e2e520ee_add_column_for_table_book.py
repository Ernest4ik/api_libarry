"""Add column for table book

Revision ID: a689e2e520ee
Revises: 357cb174e12f
Create Date: 2024-06-17 19:21:52.194885

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a689e2e520ee'
down_revision: Union[str, None] = '357cb174e12f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('author_name', sa.String(), nullable=True))
    op.add_column('book', sa.Column('edition_count', sa.Integer(), nullable=True))
    op.drop_column('book', 'price')
    op.drop_column('book', 'author')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('author', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('book', sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('book', 'edition_count')
    op.drop_column('book', 'author_name')
    # ### end Alembic commands ###