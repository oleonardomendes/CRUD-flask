"""Add user_id to task

Revision ID: ec9e682588a9
Revises: 
Create Date: 2024-07-23 22:07:34.615291

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec9e682588a9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_task_user', 'user', ['user_id'], ['id'])


    # ### end Alembic commands ###


def downgrade():
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.drop_constraint('fk_task_user', 'task', type_='foreignkey')
        batch_op.drop_column('user_id')


    # ### end Alembic commands ###
