from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.configs.dbConfig import get_db
from app.models.model import User 
from app.schemas.schema import TaskCreate, TaskUpdate, Task
from app.service.auth import  get_current_user_authorizer
from app.service.taskCrud import create_task, delete_task, get_task_by_id, get_tasks, update_task, update_task_status 
 
task = APIRouter()



@task.post("/tasks", response_model= Task)
def createTask(request: TaskCreate, current_user: User = Depends(get_current_user_authorizer), db: Session = Depends(get_db)):
    print("current_user", current_user)
    user_id = int(current_user['sub'])
    created_task = create_task(db, request, user_id)
    return created_task

@task.get("/tasks")
def getTasks(current_user: User = Depends(get_current_user_authorizer), db: Session = Depends(get_db)):
    user_id = int(current_user['sub'])
    dbResp = get_tasks(db, user_id)
    return dbResp

@task.get("/tasks/{task_id}", response_model=Task)
def getTask(task_id: int, current_user: User = Depends(get_current_user_authorizer), db: Session = Depends(get_db)):
    user_id = int(current_user['sub'])
    dbResp = get_task_by_id(db, task_id, user_id)    
    return dbResp

@task.put("/tasks/{task_id}", response_model=Task)
def updateTask(task_id: int, request: TaskUpdate, current_user: User = Depends(get_current_user_authorizer), db: Session = Depends(get_db)):
    user_id = int(current_user['sub'])
    dbResp = update_task(db, task_id, user_id, request)    
    return dbResp

@task.patch("/tasks/{task_id}/status", response_model=Task)
def updateTaskStatus(task_id: int, current_user: User = Depends(get_current_user_authorizer), db: Session = Depends(get_db)):
    user_id = int(current_user['sub'])
    dbResp = update_task_status(db, task_id, user_id)    
    return dbResp


@task.delete("/tasks/{task_id}")
def deleteTask(task_id: int, current_user: User = Depends(get_current_user_authorizer), db: Session = Depends(get_db)):
    user_id = int(current_user['sub'])
    delete_task(db, task_id, user_id)
    return {"message": "Task deleted successfully"}
 