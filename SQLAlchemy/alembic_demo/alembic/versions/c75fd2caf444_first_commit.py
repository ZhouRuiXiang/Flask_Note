"""first commit

Revision ID: c75fd2caf444
Revises: 
Create Date: 2019-08-13 15:52:59.983200

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c75fd2caf444'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # op.create_table('user',
    # sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    # sa.Column('username', sa.String(length=20), nullable=False),
    # sa.PrimaryKeyConstraint('id')
    # )
    # op.create_table('article',
    # sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    # sa.Column('title', sa.String(length=50), nullable=False),
    # sa.Column('uid', sa.Integer(), nullable=False),
    # sa.ForeignKeyConstraint(['uid'], ['user.id'], ),
    # sa.PrimaryKeyConstraint('id')
    # )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('article')
    op.drop_table('user')
    # ### end Alembic commands ###
