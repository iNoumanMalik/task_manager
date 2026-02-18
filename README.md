# Task Management System API

A professional backend Task Management System built with **FastAPI**, **Pydantic**, **SQLAlchemy**, **Pytest** and **SQLite**.

This project demonstrates clean architecture, proper validation, database persistence, filtering, pagination, and scalable backend design suitable for real-world applications.

---

## 🚀 Features

### Task Operations

* Create a task
* Get all tasks
* Get a task by ID
* Update a task by ID
* Delete a task by ID

### Task Fields

Each task includes:

* `id`
* `title`
* `description`
* `status` (pending, in_progress, completed)
* `priority` (low, medium, high)
* `due_date`
* `created_at`
* `updated_at`

### Validation

* Title must not be empty
* Status must be from a fixed list
* Priority must be validated
* Due date must be a valid future date

### Query Capabilities

* Filter by status
* Filter by priority
* Search by title or description
* Sort by `due_date` or `created_at`
* Pagination using `limit` and `offset`

---

## 🏗 Project Structure

```
task_manager/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── services.py
│   └── routes.py
├── tests/
│   ├── confest.py
│   ├── test_tasks.py
│
└── requirements.txt
```

### Architecture Principles

* Separation of concerns
* Business logic separated from routes
* Dependency injection for database sessions
* ORM-based database interaction
* Clean and reusable code

---

## 🛠 Tech Stack

* FastAPI (API framework)
* Pydantic (Validation & schemas)
* SQLAlchemy (ORM)
* Pytest
* SQLite (Database)

---

## ⚙️ Installation

1. Create virtual environment:

```
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

2. Install dependencies:

```
pip install fastapi uvicorn sqlalchemy pydantic
```

3. Run the server:

```
uvicorn app.main:app --reload
```

4. Open API docs:

```
http://127.0.0.1:8000/docs
```

---

## 📌 API Overview

### Create Task

`POST /tasks`

### Get All Tasks

`GET /tasks`

Supports:

* `status`
* `priority`
* `search`
* `limit`
* `offset`
* `sort_by`

### Get Task by ID

`GET /tasks/{task_id}`

### Update Task

`PUT /tasks/{task_id}`

### Delete Task

`DELETE /tasks/{task_id}`

### Run Test

python3 -m pytest -s
---

## 🎯 Goals of This Project

* Practice production-style FastAPI development
* Implement clean backend architecture
* Apply validation and database constraints
* Handle errors properly with correct HTTP status codes
* Build scalable, maintainable backend code

---

## 🔮 Future Improvements

* JWT Authentication
* PostgreSQL support
* Docker configuration
* Unit testing
* Async SQLAlchemy integration

---

