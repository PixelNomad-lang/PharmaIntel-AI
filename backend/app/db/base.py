from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# Crucial: Import all models at the bottom so Base.metadata is populated for Alembic
from app.db.models import *  # noqa: F401, F403