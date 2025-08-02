from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, func
from app.db import Base

class CredentialORM(Base):
    __tablename__ = "credentials"
    id             = Column(Integer, primary_key=True, autoincrement=True, index=True)
    service_name   = Column(String, nullable=True)
    is_bot         = Column(Boolean, default=False)
    user_id        = Column(String, nullable=True)
    connection_id  = Column(String, nullable=True)

    access_token   = Column(Text, nullable=True)
    refresh_token  = Column(Text, nullable=True)

    created_at     = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    updated_at     = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False)

    expires_at = Column(
        DateTime(timezone=True),
        nullable=True
    )