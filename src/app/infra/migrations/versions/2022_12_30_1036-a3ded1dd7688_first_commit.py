"""First commit

Revision ID: a3ded1dd7688
Revises: 
Create Date: 2022-12-30 10:36:30.138410

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a3ded1dd7688'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('beer')
    op.drop_table('account')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account',
                    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
                    sa.Column('username', sa.VARCHAR(length=64), autoincrement=False, nullable=False),
                    sa.Column('email', sa.VARCHAR(length=64), autoincrement=False, nullable=False),
                    sa.Column('_hashed_password', sa.VARCHAR(length=1024), autoincrement=False, nullable=True),
                    sa.Column('_hash_salt', sa.VARCHAR(length=1024), autoincrement=False, nullable=True),
                    sa.Column('is_verified', sa.BOOLEAN(), autoincrement=False, nullable=False),
                    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
                    sa.Column('is_logged_in', sa.BOOLEAN(), autoincrement=False, nullable=False),
                    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
                    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
                    sa.PrimaryKeyConstraint('id', name='account_pkey'),
                    sa.UniqueConstraint('email', name='account_email_key'),
                    sa.UniqueConstraint('username', name='account_username_key')
                    )
    op.create_table('beer',
                    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
                    sa.Column('name', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
                    sa.Column('ibu', sa.VARCHAR(length=5), autoincrement=False, nullable=False),
                    sa.Column('style', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
                    sa.Column('description', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
                    sa.Column('alcohol_tenor', sa.VARCHAR(length=5), autoincrement=False, nullable=False),
                    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
                    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
                    sa.PrimaryKeyConstraint('id', name='beer_pkey')
                    )
    # ### end Alembic commands ###
