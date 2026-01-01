from sqlalchemy import Column, Date, Numeric, Text, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.database import Base

class Request(Base):
    __tablename__ = "request"

    request_uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    request_date = Column(Date)
    request_company_uuid = Column(UUID, ForeignKey("company.company_uuid"))
    target_company_uuid = Column(UUID, ForeignKey("company.company_uuid"))
    carbon_unit_price = Column(Numeric)
    carbon_quantity = Column(Numeric)
    request_reason = Column(Text)
    request_type = Column(String)
    status = Column(String)
