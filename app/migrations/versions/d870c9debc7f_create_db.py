"""create db

Revision ID: d870c9debc7f
Revises: e8c7b2d1cea4
Create Date: 2023-09-07 17:30:47.802718

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd870c9debc7f'
down_revision: Union[str, None] = 'e8c7b2d1cea4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
