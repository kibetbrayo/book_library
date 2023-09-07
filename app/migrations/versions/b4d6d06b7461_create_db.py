"""create db

Revision ID: b4d6d06b7461
Revises: d870c9debc7f
Create Date: 2023-09-07 17:34:53.223451

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b4d6d06b7461'
down_revision: Union[str, None] = 'd870c9debc7f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
