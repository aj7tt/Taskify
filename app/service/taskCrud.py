from fastapi import HTTPException
from sqlalchemy.orm import Session 
from app.models.model import User, Task
from app.schemas.schema import TaskCreate, TaskUpdate


def create_task(db: Session, request: dict, user_id: int) -> Task:
    #create a new task    
    try:
        task = Task(
            task_name=request.task_name,
            description=request.description,
            due_date=request.due_date,
            status=request.status,
            user_id=user_id   
        )
        db.add(task)
        db.commit()
        db.refresh(task)
        return task
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def get_tasks(db: Session, user_id: int):
    # Get all tasks associated with the user
    try:
        tasks = db.query(Task).filter(Task.user_id == user_id).all()
        return tasks
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_task_by_id(db: Session, task_id: int, user_id: int):
    # Get a specific task by ID associated with the user
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == user_id).first()
    print(str(task))
    if task is None:
        raise HTTPException(status_code=404, detail=f"Task not found for userId {user_id}")
    return task

def update_task_status(db: Session, task_id: int, user_id: int):
    try:
        # Retrieve the task by ID and user_id
        task = get_task_by_id(db, task_id, user_id)

        # Update  the status field
        # task.status = status
        task.status = not task.status  # Toggle the status

        # Commit the changes to the database
        db.commit()
        db.refresh(task)
        return task
    except HTTPException:
        raise HTTPException(status_code=404, detail=f"Task not found for userId {user_id}")   

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def update_task(db: Session, task_id: int, user_id: int, task_data: TaskUpdate) -> Task:
    try:
        # Get the task by ID and user_id
        task = get_task_by_id(db, task_id, user_id)
        
        for field, value in task_data.dict(exclude_unset=True).items():
            setattr(task, field, value)
        db.commit()
        db.refresh(task)
        return task
    except HTTPException:
        raise HTTPException(status_code=404, detail=f"Task not found for userId {user_id}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def delete_task(db: Session, task_id: int, user_id: int):
    try:
        # Get the task by ID and user_id
        task = get_task_by_id(db, task_id, user_id)

        # Delete the task
        db.delete(task)
        db.commit()
    except HTTPException:
        raise HTTPException(status_code=404, detail=f"Task not found for userId {user_id}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))