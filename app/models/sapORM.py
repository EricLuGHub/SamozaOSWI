from sqlalchemy import Column, Integer, DateTime, ForeignKey, func
from app.db import Base

class SapORM(Base):
    __tablename__ = "sap"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    badge_id = Column(
        Integer,
        ForeignKey("badges.badge_id", ondelete="CASCADE"),
        nullable=False
    )
    permissions = Column(
        Integer,
        nullable=False
    )
    awarded_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )