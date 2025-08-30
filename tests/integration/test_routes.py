import pytest
from unittest.mock import patch


@pytest.mark.integration
def test_create_task(client):
    response = client.post("/tasks", json={"title": "test", "done": False})
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "test" and data["done"] is False


@pytest.mark.integration
def test_create_task_without_fields(client):
    response = client.post("/tasks", json={})
    assert response.status_code == 400
    assert b"errors" in response.data


@pytest.mark.integration
def test_create_task_commit_exception(client):
    with patch("task_api.models.task.db.session.commit") as mocked_commit:
        mocked_commit.side_effect = Exception("DB error")

        response = client.post("/tasks", json={"title": "test", "done": False})
        assert response.status_code == 500
        assert b"DB error" in response.data


@pytest.mark.integration
def test_get_tasks(client):
    response = client.get("/tasks")
    assert response.status_code == 200

    data = response.get_json()
    assert isinstance(data, list)


@pytest.mark.integration
def test_delete_task(client):
    create_task_response = client.post("/tasks", json={"title": "test", "done": False})
    task_id = create_task_response.get_json()["id"]

    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200

    data = response.get_json()
    assert data["id"] == task_id


@pytest.mark.integration
def test_delete_task_commit_exception(client):
    create_task_response = client.post("/tasks", json={"title": "test", "done": False})
    task_id = create_task_response.get_json()["id"]

    with patch("task_api.models.task.db.session.commit") as mocked_commit:
        mocked_commit.side_effect = Exception("DB error")

        response = client.delete(f"/tasks/{task_id}")
        assert response.status_code == 500
        assert b"DB error" in response.data


@pytest.mark.integration
def test_update_task(client):
    create_task_response = client.post("/tasks", json={"title": "test", "done": False})
    task_id = create_task_response.get_json()["id"]

    response = client.patch(f"/tasks/{task_id}", json={"done": True})
    assert response.status_code == 200

    data = response.get_json()
    assert data["id"] == task_id and data["title"] == "test" and data["done"] is True


@pytest.mark.integration
def test_update_task_without_fields(client):
    create_task_response = client.post("/tasks", json={"title": "test", "done": False})
    task_id = create_task_response.get_json()["id"]

    response = client.patch(f"/tasks/{task_id}", json={})
    assert response.status_code == 400
    assert b"errors" in response.data


@pytest.mark.integration
def test_update_task_commit_exception(client):
    create_task_response = client.post("/tasks", json={"title": "test", "done": False})
    task_id = create_task_response.get_json()["id"]

    with patch("task_api.models.task.db.session.commit") as mocked_commit:
        mocked_commit.side_effect = Exception("DB error")

        response = client.patch(
            f"/tasks/{task_id}", json={"title": "Test", "done": False}
        )
        assert response.status_code == 500
        assert b"DB error" in response.data
