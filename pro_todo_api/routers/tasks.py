from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, schemas
from database import get_db

router = APIRouter (prefix="/tasks", tags=["tasks"])

@router.post ("/{user_id}", response_model=schemas.TaskResponse)
def create_task(user_id: int, task: schemas.TaskCreate, db: Session = Depends (get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    new_task = models.Task(**task.dict(), owner_id=user_id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    
    return new_task

@router.get("/{user_id}", response_model=List[schemas.TaskResponse])
def read_tasks(user_id: int, db: Session = Depends(get_db)):
    tasks=db.query(models.Task).filter (models.Task.owner_id == user_id).all()
    return tasks


@router.get('', response_model=List[schemas.TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(models.Task).all()
    return tasks

@router.patch("/{task_id}", response_model=schemas.TaskResponse)
def update_task(task_id: int, task_update: schemas.TaskUpdate, db: Session = Depends(get_db)):

    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if task_update.title is not None:
        task.title = task_update.title
    if task_update.description is not None:
        task.description = task_update.description
    if task_update.completed is not None:
        task.completed = task_update.completed

    db.commit()
    db.refresh(task)

    return task

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):

    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}



# task: schemas.TaskResponse,