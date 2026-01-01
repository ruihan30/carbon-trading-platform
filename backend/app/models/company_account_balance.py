from sqlalchemy import Column, Numeric, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.database import Base

class CompanyAccountBalance(Base):
    __tablename__ = "company_account_balance"

    balance_uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    company_uuid = Column(UUID, ForeignKey("company.company_uuid"))
    carbon_balance = Column(Numeric)
    cash_balance = Column(Numeric)
    updated_at = Column(DateTime)
