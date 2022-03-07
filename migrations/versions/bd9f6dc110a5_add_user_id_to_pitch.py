"""add user id to pitch

Revision ID: bd9f6dc110a5
Revises: a426b6bb4d3f
Create Date: 2022-03-07 12:52:39.994766

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd9f6dc110a5'
down_revision = 'a426b6bb4d3f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitch', sa.Column('title', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('pitch_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'pitch', ['pitch_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'pitch_id')
    op.drop_column('pitch', 'title')
    # ### end Alembic commands ###
