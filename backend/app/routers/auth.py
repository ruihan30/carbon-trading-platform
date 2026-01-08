from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user import User
from app.schemas.user import UserLoginResponse, UserLoginRequest
from app.core.security import verify_password, create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(tags=["Auth"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# @router.post("/login", response_model=UserLoginResponse)
# def login(data: UserLoginRequest, db: Session = Depends(get_db)):
#     user = db.query(User).filter(User.email == data.email).first()

#     if not user or not verify_password(data.password, user.password):
#         raise HTTPException(status_code=401, detail="Invalid credentials")

#     token = create_access_token({"sub": str(user.user_uuid)})

#     return {
#         "access_token": token,
#         "token_type": "bearer"
#     }

@router.post("/login", response_model=UserLoginResponse)
# Change 'data: UserLoginRequest' to 'data: OAuth2PasswordRequestForm = Depends()'
def login(data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    print(f"Login attempt for: {data.username}")
    # Note: data.username is used instead of data.email
    user = db.query(User).filter(User.email == data.username).first()

    if not user or not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": str(user.user_uuid)})
    return {"access_token": token, "token_type": "bearer"}
