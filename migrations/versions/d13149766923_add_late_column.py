"""add late column

Revision ID: d13149766923
Revises: a53bfdfc0a8f
Create Date: 2021-03-11 09:27:26.970808

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd13149766923'
down_revision = 'a53bfdfc0a8f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('performed_intervention', sa.Column('late', sa.Integer(), nullable=True))
    op.create_unique_constraint(None, 'user', ['friendly'])


def downgrade():
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('performed_intervention', 'late')
