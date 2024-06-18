"""json

Revision ID: c55cd8c4a6b5
Revises: 97fcd3f0c432
Create Date: 2024-04-12 23:53:46.145730

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c55cd8c4a6b5'
down_revision = '97fcd3f0c432'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
  op.create_table('images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('motor_id', sa.Integer(), nullable=True),
    sa.Column('image_url', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['motor_id'], ['motors.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
  op.execute("ALTER TABLE motors ALTER COLUMN images TYPE JSON USING images::json")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('motors', schema=None) as batch_op:
        batch_op.alter_column('images',
               existing_type=sa.JSON(),
               type_=sa.VARCHAR(),
               existing_nullable=True)

    # ### end Alembic commands ###
