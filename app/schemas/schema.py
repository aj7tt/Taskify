# Import necessary modules and packages
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# User schema
class UserBase(BaseModel):
    username: str = Field(..., description="User's username")
    password: str = Field(..., description="User's password")

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
    task_name: str = Field(..., description="Task name")
    description: Optional[str] = Field(None, description="Task description")
    due_date: datetime = Field(..., description="Due date of the task")
    status: bool = Field(..., description="Task status (completed or not)") 

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class Task(TaskBase):
    class Config:
        orm_mode = True
