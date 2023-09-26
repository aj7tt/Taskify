from datetime import datetime, timedelta 
from sqlalchemy.orm import Session
from passlib.context import CryptContext  # For password hashing
from jose import jwt

#sensitive data 
# JWT settings
SECRET_KEY = "Aa1$2Bb3*Cc4Dd5Ee6Ff7Gg8Hh9Ii0JjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
ALGORITHM = "HS256"
TOKEN_EXP_MIN = 60

# Create a CryptContext instance for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_jwt_token(user_id: int, username: str) -> str:
    expiration = datetime.utcnow() + timedelta(minutes=TOKEN_EXP_MIN)
    payload = {
        "sub": user_id,
        "username": username,
        "exp": expiration
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token