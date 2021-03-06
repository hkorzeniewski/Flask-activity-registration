"""empty message

Revision ID: c8b93fe68601
Revises: 
Create Date: 2021-03-05 18:00:44.368436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8b93fe68601'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cardio',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cardio_name', sa.String(length=150), nullable=True),
    sa.Column('place', sa.String(length=100), nullable=True),
    sa.Column('distance', sa.Integer(), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('activity', sa.Column('duration', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('activity', 'duration')
    op.drop_table('cardio')
    # ### end Alembic commands ###
