from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from app.database import Base

class User(Base):
    __tablename__ = "users"

    user_uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_name = Column(String)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    company_uuid = Column(UUID, ForeignKey("company.company_uuid"))
    created_at = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    last_login = Column(DateTime(timezone=True), nullable=True)
