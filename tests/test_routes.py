import pytest
from task_api.app import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True
    })
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def test_create_task(client):
    response = client.post("/tasks", json={
        "title": "test",
        "done": False
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "test" and data["done"] is False

def test_get_tasks(client):
    response = client.get("/tasks")
    assert response.status_code == 200

    data = response.get_json()
    assert isinstance(data, list)

def test_delete_task(client):
    create_task_response = client.post("/tasks", json={
        "title": "test",
        "done": False
    })
    task_id = create_task_response.get_json()["id"]

    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
    
    data = response.get_json()
    assert data["id"] == task_id


def test_update_task(client):
    create_task_response = client.post("/tasks", json={
        "title": "test",
        "done": False
    })
    task_id = create_task_response.get_json()["id"]

    response = client.patch(f"/tasks/{task_id}", json={
        "done": True
    })
    assert response.status_code == 200

    data = response.get_json()
    assert data["id"] == task_id and data["title"] == "test" and data["done"] is True