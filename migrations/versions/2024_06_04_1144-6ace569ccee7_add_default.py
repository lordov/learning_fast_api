"""Add default

Revision ID: 6ace569ccee7
Revises: f1035df1258b
Create Date: 2024-06-04 11:44:57.993386

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6ace569ccee7'
down_revision: Union[str, None] = 'f1035df1258b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('operation', 'figi',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('operation', 'figi',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
