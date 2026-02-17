# schema control input validation, format response and data rules
from pydantic import BaseModel, field_validator,ConfigDict
from datetime import datetime
from typing import Optional # used to declare that a variable or field can either be of a certain type or None.
from .models import TaskStatus, TaskPriority

# BaseModel provides Type validation, Converts incoming data (like JSON) into proper Python objects and vice versa and Raises clear validation errors
class TaskBase(BaseModel): 

    # This tells Pydantic what fields exist, their types, and whether they’re optional or required.
    title: str
    description: Optional[str] = None
    status: TaskStatus
    priority: TaskPriority
    due_date: datetime

    # Whenever the title field is set, run this function to check it.
    @field_validator("title")
    def title_not_empty(cls,value): #cls-> model class itself
        if not value.strip(): # this give us True if the string has no leading and trailing space, False if it has spaces and that's why on False we raise error
            raise ValueError("Title must not be empty")
        return value
    
    @field_validator("due_date")
    def due_date_future(cls,value):
        if value <= datetime.utcnow():
            raise ValueError("Due date must be in the future")
        return value

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None
    due_date: Optional[datetime] = None


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    status: str
    priority: str
    due_date: datetime | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

    # class Config:  # the translator that tells Pydantic how to read ORM objects and turn them into JSON.
    #     from_attributes = True
