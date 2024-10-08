"""Migration to fix issues with creating budget

Revision ID: a45b1af2a8ce
Revises: 5f016095eb36
Create Date: 2024-10-08 16:22:46.432745

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a45b1af2a8ce'
down_revision: Union[str, None] = '5f016095eb36'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('budgets', 'total_amount',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               type_=sa.Integer(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('budgets', 'total_amount',
               existing_type=sa.Integer(),
               type_=sa.DOUBLE_PRECISION(precision=53),
               nullable=True)
    # ### end Alembic commands ###
