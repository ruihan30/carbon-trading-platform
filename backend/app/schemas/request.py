from pydantic import BaseModel
from uuid import UUID
from datetime import date

class RequestCreate(BaseModel):
    target_company_uuid: UUID
    carbon_unit_price: float
    carbon_quantity: float
    request_reason: str
    request_type: str

class RequestResponse(RequestCreate):
    request_uuid: UUID
    request_date: date
    status: str
