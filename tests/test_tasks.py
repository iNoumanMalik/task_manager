# Test Valid Task Creation
def test_create_task_valid(client):
    response = client.post(
        "/tasks/",
        json={
            "title": "Test Task",
            "description": "Testing",
            "status": "pending",
            "priority": "low",
            "due_date": "2026-02-20T12:00:00",
        },
    )

    assert response.status_code == 201
    assert response.json()["title"] == "Test Task"


# Test Invalid Task Creation (Empty Title)
def test_create_task_empty_title(client):
    response = client.post(
        "/tasks/",
        json={
            "title": "",
            "description": "Testing",
            "status": "pending",
            "priority": "low",
            "due_date": "2026-02-20T12:00:00",
        },
    )
    assert response.status_code == 422


# Invalid status
def test_create_task_invalid_status(client):
    response = client.post(
        "/tasks/",
        json={
            "title": "Test Task",
            "description": "Testing",
            "status": "wrong_status",
            "priority": "low",
            "due_date": "2026-02-20T12:00:00",
        },
    )

    assert response.status_code == 422


# Invalid priority
def test_create_task_invalid_priority(client):
    response = client.post(
        "/tasks/",
        json={
            "title": "Test Task",
            "description": "Testing",
            "status": "wrong_status",
            "priority": "low",
            "due_date": "2026-02-20T12:00:00",
        },
    )

    assert response.status_code == 422


# Fetch By ID (valid)
def test_get_task_valid(client):
    create = client.post(
        "/tasks/",
        json={
            "title": "Task 1",
            "status": "pending",
            "priority": "low",
            "due_date": "2026-02-20T12:00:00",
        },
    )

    task_id = create.json()["id"]

    response = client.get(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["id"] == task_id


# Fetch By ID (in-valid)
def test_get_task_invalid(client):
    response = client.get("/tasks/8888")
    assert response.status_code == 404


# Update Task
def test_update_task_valid(client):
    create = client.post(
        "/tasks/",
        json={
            "title": "old",
            "status": "pending",
            "priority": "low",
            "due_date": "2026-02-20T12:00:00",
        },
    )

    task_id = create.json()["id"]
    response = client.put(
        f"/tasks/{task_id}",
        json={
            "title": "updated",
            "status": "pending",
            "priority": "medium",
            "due_date": "2026-02-20T12:00:00",
        },
    )

    assert response.status_code == 200
    assert response.json()["title"] == "updated"


# Delete Task
def test_delete_task(client):
    create = client.post(
        "/tasks/",
        json={
            "title": "Delete me",
            "status": "pending",
            "priority": "low",
            "due_date": "2026-02-20T12:00:00",
        },
    )

    task_id = create.json()["id"]

    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 204

    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404


# Filtering
def test_filter_by_status(client):
    client.post(
        "/tasks/",
        json={
            "title": "Task A",
            "status": "in_progress",
            "priority": "low",
            "due_date": "2026-02-20T12:00:00",
        },
    )

    client.post(
        "/tasks/",
        json={
            "title": "Task B",
            "status": "completed",
            "priority": "low",
            "due_date": "2026-02-20T12:00:00",
        },
    )

    response = client.get("/tasks/?status=in_progress")
    assert response.status_code == 200
    assert len(response.json()) == 1


# Pagination
def test_pagination(client):
    for i in range(5):
        client.post(
            "/tasks/",
            json={
                "title": f"Task {i}",
                "status": "pending",
                "priority": "low",
                "due_date": "2026-02-20T12:00:00",
            },
        )

    response = client.get("/tasks/?page=1&limit=2")

    assert response.status_code == 200
    assert len(response.json()) == 2


def test_past_due_date(client):
    response = client.post(
        "/tasks/",
        json={
            "title": "Late task",
            "status": "pending",
            "priority": 1,
            "due_date": "2020-01-01",
        },
    )
    assert response.status_code == 422  # validation error
