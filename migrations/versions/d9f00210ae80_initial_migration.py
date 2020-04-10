"""initial migration

Revision ID: d9f00210ae80
Revises: 
Create Date: 2020-04-09 23:38:59.950302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9f00210ae80'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('esf_fang',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('province', sa.String(length=64), nullable=True),
    sa.Column('city', sa.String(length=64), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('rooms', sa.String(length=64), nullable=True),
    sa.Column('floor', sa.String(length=16), nullable=True),
    sa.Column('toward', sa.String(length=16), nullable=True),
    sa.Column('year', sa.String(length=32), nullable=True),
    sa.Column('address', sa.String(length=128), nullable=True),
    sa.Column('area', sa.String(length=32), nullable=True),
    sa.Column('price_total', sa.String(length=32), nullable=True),
    sa.Column('price_unit', sa.String(length=32), nullable=True),
    sa.Column('origin_url', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('new_house_fang',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('province', sa.String(length=64), nullable=True),
    sa.Column('city', sa.String(length=64), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('price', sa.String(length=64), nullable=True),
    sa.Column('rooms', sa.String(length=64), nullable=True),
    sa.Column('area', sa.String(length=32), nullable=True),
    sa.Column('address', sa.String(length=128), nullable=True),
    sa.Column('district', sa.String(length=64), nullable=True),
    sa.Column('sale', sa.String(length=64), nullable=True),
    sa.Column('origin_url', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('new_house_fang')
    op.drop_table('esf_fang')
    # ### end Alembic commands ###
