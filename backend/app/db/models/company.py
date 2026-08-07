from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.models.base_model import BaseModel


class Company(BaseModel):

    __tablename__ = "companies"

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True
    )

    website: Mapped[str | None] = mapped_column(
        String(500)
    )

    industry: Mapped[str | None] = mapped_column(
        String(100)
    )