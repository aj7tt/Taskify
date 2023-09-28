# Import necessary modules and packages
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy import Column, Date

from app.configs.dbConfig import Base

# Define the User model
class User(Base):
    __tablename__ = 'users'

    # Primary key
    id = Column(Integer, primary_key=True)

    # User properties
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String, nullable=False)

    # Relationship to tasks
    tasks = relationship("Task", back_populates="user")

# Define the Task model
class Task(Base):
    __tablename__ = 'tasks'

    # Primary key
    id = Column(Integer, primary_key=True)

    # Task properties
    task_name = Column(String(255), nullable=False)
    description = Column(String)
    due_date = Column(Date)
    status = Column(Boolean, default=False)

    # Foreign key to link to the User model
    user_id = Column(Integer, ForeignKey('users.id'))

    # Relationship to user
    user = relationship("User", back_populates="tasks")
