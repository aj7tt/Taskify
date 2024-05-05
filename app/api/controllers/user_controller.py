from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.configs.dbConfig import get_db
from app.models.model import User

from app.schemas.schema import UserCreate, UserLogin
from app.service.auth import create_jwt_token, hash_password, verify_password
from app.service.userCrud import create_user, is_username_taken

user = APIRouter()


@user.post("/register", response_model=dict)
def register(request: UserCreate, db: Session = Depends(get_db)):
    # Check if the username is already taken
    if is_username_taken(db, request.username):
        raise HTTPException(status_code=400, detail="Username is already registered")
    
    # Hash the user's password before storing it in the database
    hashed_password = hash_password(request.password)
    
    # Create a new user data dictionary with the hashed password
    user_data = request.dict()
    user_data['password'] = hashed_password
    
    # Create a new user in the database using the create_user function
    dbResp = create_user(db, user_data)
    
    # Return only the username and id
    return {"id": dbResp.id, "username": dbResp.username}



@user.post("/login", response_model=dict)
def getToken(request: UserLogin, db: Session = Depends(get_db)):
    # Check if the username is present in database or not 
    dbResp = is_username_taken(db, request.username)
    
    if dbResp is None or not verify_password(request.password, dbResp.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    # Generate a JWT token for the user
    token = create_jwt_token(user_id=dbResp.id, username=dbResp.username)
    
    return {"access_token": token, "token_type": "bearer"}
