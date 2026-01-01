from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.company_account_balance import CompanyAccountBalance
from app.models.company import Company
from app.schemas.balance import BalanceResponse
from app.core.security import get_current_user

router = APIRouter(tags=["Balances"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/balances", response_model=BalanceResponse)
def get_balances(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    balance = (
        db.query(CompanyAccountBalance, Company)
        .join(Company, Company.company_uuid == CompanyAccountBalance.company_uuid)
        .filter(Company.company_uuid == current_user.company_uuid)
        .first()
    )

    return {
        "company_name": balance.Company.company_name,
        "carbon_balance": balance.CompanyAccountBalance.carbon_balance,
        "cash_balance": balance.CompanyAccountBalance.cash_balance
    }
