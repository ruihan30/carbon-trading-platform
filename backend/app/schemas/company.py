from pydantic import BaseModel
from uuid import UUID

class CompanyResponse(BaseModel):
    company_uuid: UUID
    company_name: str
