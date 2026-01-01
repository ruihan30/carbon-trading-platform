from pydantic import BaseModel, EmailStr
from uuid import UUID

class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str

class UserLoginResponse(BaseModel):
    access_token: str
    token_type: str

class UserResponse(BaseModel):
    user_uuid: UUID
    user_name: str
    email: EmailStr
    company_uuid: UUID
