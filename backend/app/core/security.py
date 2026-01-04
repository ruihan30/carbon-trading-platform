from datetime import datetime, timedelta
from jose import jwt, JWTError
import hashlib
import bcrypt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.database import SessionLocal
from app.models.user import User
from app.core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def hash_password(password: str) -> str:
    # 1. Pre-hash with SHA-256 to solve the 72-byte limit forever
    # This turns any password into a 64-character hex string
    pw_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
    
    # 2. Hash with Bcrypt directly (bypassing the broken Passlib)
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(pw_hash.encode("utf-8"), salt)
    
    return hashed_password.decode("utf-8")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    # 1. Pre-hash the incoming password the same way
    pw_hash = hashlib.sha256(plain_password.encode("utf-8")).hexdigest()
    
    # 2. Compare using bcrypt's built-in check
    return bcrypt.checkpw(
        pw_hash.encode("utf-8"), 
        hashed_password.encode("utf-8")
    )

def create_access_token(data: dict):
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data.update({"exp": expire})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_uuid = payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    db = SessionLocal()
    user = db.query(User).filter(User.user_uuid == user_uuid).first()
    db.close()

    if not user:
        raise HTTPException(status_code=401)

    return user
