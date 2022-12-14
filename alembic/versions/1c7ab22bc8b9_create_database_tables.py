"""Create database tables

Revision ID: 1c7ab22bc8b9
Revises: 
Create Date: 2022-11-14 22:45:46.102795

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c7ab22bc8b9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('animals',
    sa.Column('id', sa.Text(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('buy_value', sa.Integer(), nullable=True),
    sa.Column('days_to_produce', sa.Integer(), nullable=True),
    sa.Column('affinity_hearts', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_animals_id'), 'animals', ['id'], unique=False)
    op.create_index(op.f('ix_animals_name'), 'animals', ['name'], unique=False)
    op.create_table('seasons',
    sa.Column('id', sa.Text(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_seasons_id'), 'seasons', ['id'], unique=False)
    op.create_index(op.f('ix_seasons_name'), 'seasons', ['name'], unique=False)
    op.create_table('crops',
    sa.Column('id', sa.Text(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('buy_value', sa.Integer(), nullable=False),
    sa.Column('type', sa.Enum(name='cropgrowtypeenum'), nullable=False),
    sa.Column('days_to_harvest', sa.Integer(), nullable=False),
    sa.Column('days_before_first_harvest', sa.Integer(), nullable=True),
    sa.Column('season_id', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['season_id'], ['seasons.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_crops_id'), 'crops', ['id'], unique=False)
    op.create_index(op.f('ix_crops_name'), 'crops', ['name'], unique=False)
    op.create_table('products',
    sa.Column('id', sa.Text(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('animal_id', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['animal_id'], ['animals.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_products_id'), 'products', ['id'], unique=False)
    op.create_index(op.f('ix_products_name'), 'products', ['name'], unique=False)
    op.create_table('artisan_goods',
    sa.Column('id', sa.Text(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('type', sa.Enum(name='artisangoodstypeenum'), nullable=False),
    sa.Column('value', sa.Integer(), nullable=False),
    sa.Column('crop_id', sa.Text(), nullable=True),
    sa.Column('product_id', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['crop_id'], ['crops.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_artisan_goods_id'), 'artisan_goods', ['id'], unique=False)
    op.create_index(op.f('ix_artisan_goods_name'), 'artisan_goods', ['name'], unique=False)
    op.create_table('crops_rank',
    sa.Column('id', sa.Text(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('type', sa.Enum(name='croptypeenum'), nullable=True),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.Column('crop_id', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['crop_id'], ['crops.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_crops_rank_id'), 'crops_rank', ['id'], unique=False)
    op.create_index(op.f('ix_crops_rank_name'), 'crops_rank', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_crops_rank_name'), table_name='crops_rank')
    op.drop_index(op.f('ix_crops_rank_id'), table_name='crops_rank')
    op.drop_table('crops_rank')
    op.drop_index(op.f('ix_artisan_goods_name'), table_name='artisan_goods')
    op.drop_index(op.f('ix_artisan_goods_id'), table_name='artisan_goods')
    op.drop_table('artisan_goods')
    op.drop_index(op.f('ix_products_name'), table_name='products')
    op.drop_index(op.f('ix_products_id'), table_name='products')
    op.drop_table('products')
    op.drop_index(op.f('ix_crops_name'), table_name='crops')
    op.drop_index(op.f('ix_crops_id'), table_name='crops')
    op.drop_table('crops')
    op.drop_index(op.f('ix_seasons_name'), table_name='seasons')
    op.drop_index(op.f('ix_seasons_id'), table_name='seasons')
    op.drop_table('seasons')
    op.drop_index(op.f('ix_animals_name'), table_name='animals')
    op.drop_index(op.f('ix_animals_id'), table_name='animals')
    op.drop_table('animals')
    # ### end Alembic commands ###
