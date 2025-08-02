from sqlalchemy import Column, Integer, Text, Boolean, DateTime, Interval, func
from app.db import Base

class BadgeORM(Base):
    __tablename__ = "badges"

    badge_id = Column(Integer, primary_key=True, autoincrement=True)
    badge_name = Column(Text, nullable=True)
    badge_type = Column(Text, nullable=True)
    is_valid = Column(Boolean, nullable=True, default=True)
    created_at = Column(DateTime(timezone=True), nullable=True, server_default=func.now())
    validity_period = Column(Interval, nullable=True)
    is_ephemeral = Column(Boolean, nullable=True, default=False)