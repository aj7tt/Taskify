from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, Header 
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

#create jwt token 
def create_jwt_token(user_id: int, username: str) -> str:
    expiration = datetime.utcnow() + timedelta(minutes=TOKEN_EXP_MIN)
    user_id = str(user_id)
    
    payload = {
        "sub": user_id,
        "userName": username,
        "exp": expiration
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm= ALGORITHM)
    return token


#decode jwt token 
def get_current_user_authorizer(token: str = Header(None)) -> dict:
    # Check if the token is missing
    if token is None:
        raise HTTPException(status_code=401, detail="Token missing")

    try:
        # Attempt to decode the JWT token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        # Check if the "sub" claim is missing or not a string
        if "sub" not in payload or not isinstance(payload["sub"], str):
            raise HTTPException(status_code=401, detail="Invalid token: Missing or invalid 'sub' claim")

        # Token successfully decoded, return the payload
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
    



