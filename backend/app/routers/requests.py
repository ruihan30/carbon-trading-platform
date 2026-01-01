from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date
from app.database import SessionLocal
from app.models.request import Request
from app.models.request_received import RequestReceived
from app.schemas.request import RequestCreate, RequestResponse
from app.core.security import get_current_user

router = APIRouter(tags=["Requests"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/requests", response_model=RequestResponse)
def create_request(
    data: RequestCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    request = Request(
        request_date=date.today(),
        request_company_uuid=current_user.company_uuid,
        target_company_uuid=data.target_company_uuid,
        carbon_unit_price=data.carbon_unit_price,
        carbon_quantity=data.carbon_quantity,
        request_reason=data.request_reason,
        request_type=data.request_type,
        status="pending"
    )

    db.add(request)
    db.flush()

    received = RequestReceived(
        request_uuid=request.request_uuid,
        receiving_company_uuid=data.target_company_uuid
    )

    db.add(received)
    db.commit()
    db.refresh(request)

    return request
