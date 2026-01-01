from pydantic import BaseModel

class BalanceResponse(BaseModel):
    company_name: str
    carbon_balance: float
    cash_balance: float
