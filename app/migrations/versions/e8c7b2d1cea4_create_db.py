"""create db

Revision ID: e8c7b2d1cea4
Revises: 7ef687f710c4
Create Date: 2023-09-07 17:28:44.200059

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e8c7b2d1cea4'
down_revision: Union[str, None] = '7ef687f710c4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
