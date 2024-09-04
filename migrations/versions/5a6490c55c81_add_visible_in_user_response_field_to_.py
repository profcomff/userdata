"""Add visible_in_user_response field to Param table

Revision ID: 5a6490c55c81
Revises: 0932ab8ca14a
Create Date: 2024-09-03 10:54:14.554987

"""

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '5a6490c55c81'
down_revision = '0932ab8ca14a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('param', sa.Column('visible_in_user_response', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('param', 'visible_in_user_response')
    # ### end Alembic commands ###