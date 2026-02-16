from sqlalchemy import Integer, String, DateTime, Enum
from sqlalchemy.orm import mapped_column, Mapped
from datetime import datetime
import enum
from .database import Base


class TaskStatus(str, enum.Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"


class TaskPriority(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    status: Mapped[TaskStatus] = mapped_column(
        Enum(TaskStatus), default=TaskStatus.pending
    )  # This tells SQLAlchemy that the status column can only take values defined in the Python TaskStatus enum
    priority: Mapped[TaskPriority] = mapped_column(
        Enum(TaskPriority), default=TaskPriority.medium
    )
    due_date: Mapped[datetime] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.utcnow, onupdate=datetime.utcnow
    )


# Pydantic validates incoming data (like JSON from an API request) before you try to insert it into the database.
# SQLAlchemy constraints are like the locks on your house doors — they stop bad data from entering the database.
# Pydantic is like the security guard at the gate — it checks visitors before they even reach the door, giving clearer instructions if they don’t meet the rules.

# SQLAlchemy models = database schema.
# Pydantic models = request/response validation.
# Together, they cover both ends: clean input and safe storage.