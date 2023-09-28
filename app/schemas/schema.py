# Import necessary modules and packages
import re
from pydantic import BaseModel, Field, constr, validator
from typing import Optional
from datetime import date

class UserBase(BaseModel):
    username: constr(min_length=3, max_length=20)  # Constrain the length of username

    @validator('username')
    def validate_username(cls, value):
        if not re.match(r'^[a-zA-Z0-9]+$', value):
            raise ValueError("Username must contain only alphanumeric characters")
        return value


    password: constr(min_length=4)  # Password with minimum length of 4 characters  

class UserCreate(UserBase):
    pass

class UserLogin(UserBase):
    pass

# Token
class Token(BaseModel):
    access_token: str = Field(..., description="JWT access token")
    token_type: str = Field(..., description="Type of the token, e.g., bearer")

# Task schema
class TaskBase(BaseModel):
    task_name: constr(min_length=3)
    description: Optional[str] = Field(None, description="Task description")
    due_date: date
    status: bool = Field(default=False, description="Task status (completed or not)") 
    
    @validator('due_date')
    def validate_due_date(cls, value):
        if value is None:
            raise ValueError("due_date is required")
        return value

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class Task(TaskBase):
    class Config:
        orm_mode = True
