"""Create pitch db

Revision ID: a426b6bb4d3f
Revises: 0aaa7714b0b9
Create Date: 2022-03-07 12:43:35.365105

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a426b6bb4d3f'
down_revision = '0aaa7714b0b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitch',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=600), nullable=True),
    sa.Column('category', sa.String(length=255), nullable=True),
    sa.Column('upvotes', sa.Integer(), nullable=True),
    sa.Column('downvotes', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pitch')
    # ### end Alembic commands ###