"""add patient column to demographics

Revision ID: 5aa534afb791
Revises: f8c2163a1be0
Create Date: 2021-03-11 14:28:53.385862

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5aa534afb791'
down_revision = 'f8c2163a1be0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('demographics', sa.Column('patient', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('demographics', 'patient')
    # ### end Alembic commands ###