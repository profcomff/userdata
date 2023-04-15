"""Init

Revision ID: 9715ad3fa1d3
Revises: 
Create Date: 2023-04-05 19:55:33.189201

"""
import sqlalchemy as sa
from alembic import op


revision = '9715ad3fa1d3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'category',
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('is_deleted', sa.Boolean(), nullable=False),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'source',
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('trust_level', sa.Integer(), nullable=False),
        sa.Column('is_deleted', sa.Boolean(), nullable=False),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'param',
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('category_id', sa.Integer(), nullable=False),
        sa.Column('is_required', sa.Boolean(), nullable=False),
        sa.Column('changeable', sa.Boolean(), nullable=False),
        sa.Column('type', sa.Enum('ALL', 'LAST', 'MOST_TRUSTED', name='type', native_enum=False), nullable=True),
        sa.Column('is_deleted', sa.Boolean(), nullable=False),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ['category_id'],
            ['category.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'scope',
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('category_id', sa.Integer(), nullable=False),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ['category_id'],
            ['category.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'info',
        sa.Column('param_id', sa.Integer(), nullable=False),
        sa.Column('source_id', sa.Integer(), nullable=False),
        sa.Column('owner_id', sa.Integer(), nullable=False),
        sa.Column('value', sa.String(), nullable=False),
        sa.Column('create_ts', sa.DateTime(), nullable=False),
        sa.Column('modify_ts', sa.DateTime(), nullable=False),
        sa.Column('is_deleted', sa.Boolean(), nullable=False),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ['param_id'],
            ['param.id'],
        ),
        sa.ForeignKeyConstraint(
            ['source_id'],
            ['source.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade():
    op.drop_table('info')
    op.drop_table('scope')
    op.drop_table('param')
    op.drop_table('source')
    op.drop_table('category')
