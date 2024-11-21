"""add pessoa table

Revision ID: d868bff9686d
Revises: 
Create Date: 2024-11-20 04:30:06.366585

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'd868bff9686d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('evento',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(255), nullable=False),
    sa.Column('datahora', sa.DateTime(), nullable=False),
    sa.Column('responsavel_evento', sa.String(255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('instituicao',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(255), nullable=False),
    sa.Column('email', sa.String(255), nullable=False),
    sa.Column('endereco', sa.String(255), nullable=False),
    sa.Column('telefone', sa.String(255), nullable=False),
    sa.Column('observacao', sa.String(255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pessoa',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(255), nullable=False),
    sa.Column('email', sa.String(255), nullable=True),
    sa.Column('celular', sa.String(255), nullable=True),
    sa.Column('cpf', sa.String(255), nullable=False),
    sa.Column('datanascimento', sa.Date(), nullable=True),
    sa.Column('genero', sa.String(255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('espacoinstituicao',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_instituicao', sa.Integer(), nullable=True),
    sa.Column('nome', sa.String(255), nullable=False),
    sa.Column('capacidade', sa.String(255), nullable=False),
    sa.Column('responsavel', sa.String(255), nullable=False),
    sa.ForeignKeyConstraint(['id_instituicao'], ['instituicao.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('participacao',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_evento', sa.Integer(), nullable=True),
    sa.Column('id_pessoa', sa.Integer(), nullable=True),
    sa.Column('tipo', sa.String(255), nullable=False),
    sa.ForeignKeyConstraint(['id_evento'], ['evento.id'], ),
    sa.ForeignKeyConstraint(['id_pessoa'], ['pessoa.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('alocacao',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_evento', sa.Integer(), nullable=True),
    sa.Column('id_instituicao', sa.Integer(), nullable=True),
    sa.Column('id_espaco', sa.Integer(), nullable=True),
    sa.Column('datahora', sa.DateTime(), nullable=False),
    sa.Column('status', sa.String(255), nullable=False),
    sa.Column('responsavel_local', sa.String(255), nullable=False),
    sa.ForeignKeyConstraint(['id_espaco'], ['espacoinstituicao.id'], ),
    sa.ForeignKeyConstraint(['id_evento'], ['evento.id'], ),
    sa.ForeignKeyConstraint(['id_instituicao'], ['instituicao.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('ix_users_email', table_name='users')
    op.drop_index('ix_users_id', table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_users_id', 'users', ['id'], unique=False)
    op.create_index('ix_users_email', 'users', ['email'], unique=True)
    op.drop_table('alocacao')
    op.drop_table('participacao')
    op.drop_table('espacoinstituicao')
    op.drop_table('pessoa')
    op.drop_table('instituicao')
    op.drop_table('evento')
    # ### end Alembic commands ###
