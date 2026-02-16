from sqlalchemy.orm import Session
from . import models


def create_task(db: Session, task_data):
    task = models.Task(**task_data.dict())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def get_tasks(
    db: Session,
    status=None,
    priority=None,
    search=None,
    limit=10,
    offset=0,
    sort_by="created_at",
):
    query = db.query(models.Task)

    if status:
        query = query.filter(models.Task.status == status)

    if priority:
        query = query.filter(models.Task.priority == priority)

    if search:
        query = query.filter(
            (models.Task.title.contains(search))
            | (models.Task.description.contains(search))
        )

    if sort_by in ["due_date", "created_at"]:
        query = query.order_by(getattr(models.Task, sort_by))

    return query.offset(offset).limit(limit).all()


# setattr is a built‑in Python function that lets you dynamically set an attribute on an object. setattr(object, attribute_name, value)
def update_task(db: Session, task, updated_data):
    for key, value in updated_data.dict(exclude_unset=True).items():
        setattr(task, key, value)

    db.commit()
    db.refresh(
        task
    )  # It reloads the object from the database to ensure your Python object reflects the latest state
    return task


def delete_task(db: Session, task):
    db.delete(task)
    db.commit()
