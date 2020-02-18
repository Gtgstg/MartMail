"""empty message

Revision ID: 04e87c2fc94e
Revises: 96ee95a1998d
Create Date: 2020-02-18 21:57:48.112825

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04e87c2fc94e'
down_revision = '96ee95a1998d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('purchaseDate', sa.DateTime(), nullable=True),
    sa.Column('totalPrice', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order')
    # ### end Alembic commands ###
