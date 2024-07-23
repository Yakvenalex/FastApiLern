"""add

Revision ID: 3bc793e24f23
Revises: 3e41a2ab1fca
Create Date: 2024-07-23 13:42:46.733375

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3bc793e24f23'
down_revision: Union[str, None] = '3e41a2ab1fca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
