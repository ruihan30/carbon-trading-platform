from sqlalchemy import Column, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.database import Base

class RequestReceived(Base):
    __tablename__ = "request_received"

    request_received_uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    request_uuid = Column(UUID, ForeignKey("request.request_uuid"))
    receiving_company_uuid = Column(UUID, ForeignKey("company.company_uuid"))
    alert_shown = Column(Boolean, default=False)
    created_at = Column(DateTime)
