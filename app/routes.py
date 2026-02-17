from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .database import get_db
from typing import List
from . import schemas, services


# FastAPI automatically generates interactive API docs (Swagger UI and ReDoc).
# tags=["Tasks"] tells FastAPI: “Group all endpoints in this router under the section called ‘Tasks’ in the docs.”


router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/",response_model=schemas.TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return services.create_task(db,task)

@router.get("/",response_model=List[schemas.TaskResponse])
def get_tasks(
    status: schemas.TaskStatus = None,
    priority: schemas.TaskPriority = None,
    search: str = None,
    limit: int = 10,
    offset: int = 0,
    sort_by:str = "created_at",
    db: Session = Depends(get_db), 
    ):
    return services.get_tasks(db,status,priority,search,limit,offset,sort_by)


@router.get("/{task_id}",response_model=schemas.TaskResponse)
def get_task(task_id: int, db:Session = Depends(get_db)):
    task =  services.get_task(db,task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}",response_model=schemas.TaskResponse)
def update_task(task_id:int,updated_data:schemas.TaskUpdate, db:Session = Depends(get_db)):
    task = services.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return services.update_task(db, task, updated_data)

@router.delete("/{task_id}",status_code=status.HTTP_204_NO_CONTENT)

def delete_task(task_id:int, db:Session = Depends(get_db)):
    task = services.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return services.delete_task(db,task)