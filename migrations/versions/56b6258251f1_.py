"""empty message

Revision ID: 56b6258251f1
Revises: 146cc28d11b8
Create Date: 2020-02-19 17:46:19.893267

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56b6258251f1'
down_revision = '146cc28d11b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('customers', 'address')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customers', sa.Column('address', sa.VARCHAR(length=1000), autoincrement=False, nullable=True))
    # ### end Alembic commands ###