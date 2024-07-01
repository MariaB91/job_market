# Script de migration en Python avec Alembic pour MySQL
from alembic import op
import sqlalchemy as sa

# Révision identifiant
revision = '001'
down_revision = None

def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('username', sa.String(50), unique=True, nullable=False),
        sa.Column('password', sa.String(255), nullable=False),
        sa.Column('email', sa.String(100), unique=True, nullable=False)
    )
    op.create_table(
        'jobs',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('title', sa.String(100), nullable=False),
        sa.Column('company', sa.String(100), nullable=False),
        sa.Column('location', sa.String(100), nullable=False),
        sa.Column('description', sa.Text),
        sa.Column('source', sa.String(50)),
        sa.Column('date_posted', sa.Date)
    )
    op.create_table(
        'recommendations',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id')),
        sa.Column('job_id', sa.Integer, sa.ForeignKey('jobs.id')),
        sa.Column('score', sa.Float)
    )

def downgrade():
    op.drop_table('recommendations')
    op.drop_table('jobs')
    op.drop_table('users')
