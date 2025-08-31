import pytest
import logging
from unittest.mock import patch

logger = logging.getLogger(__name__)


@pytest.mark.integration
def test_create_task(client):
    logger.info("Starting test_create_task...")
    response = client.post("/tasks", json={"title": "test", "done": False})
    logger.debug(
        f"Response status code: {response.status_code} and data: {response.data}"
    )
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "test" and data["done"] is False
    logger.info("test_create_task completed successfully.")


@pytest.mark.integration
def test_create_task_without_fields(client):
    logger.info("Starting test_create_task_without_fields...")
    response = client.post("/tasks", json={})
    logger.debug(
        f"Response status code: {response.status_code} and data: {response.data}"
    )
    assert response.status_code == 400
    assert b"errors" in response.data
    logger.info("test_create_task_without_fields completed successfully.")


@pytest.mark.integration
def test_create_task_commit_exception(client):
    logger.info("Starting test_create_task_commit_exception...")
    with patch("task_api.models.task.db.session.commit") as mocked_commit:
        mocked_commit.side_effect = Exception("DB error")

        response = client.post("/tasks", json={"title": "test", "done": False})
        logger.debug(
            f"Response status code: {response.status_code} and data: {response.data}"
        )
        assert response.status_code == 500
        assert b"DB error" in response.data
    logger.info("test_create_task_commit_exception completed successfully.")


@pytest.mark.integration
def test_get_tasks(client):
    logger.info("Starting test_get_tasks...")
    response = client.get("/tasks")
    logger.debug(f"Response status code: {response.status_code}")
    assert response.status_code == 200

    data = response.get_json()
    assert isinstance(data, list)
    logger.info("test_get_tasks completed successfully.")


@pytest.mark.integration
def test_delete_task(client):
    logger.info("Starting test_delete_task...")
    create_task_response = client.post("/tasks", json={"title": "test", "done": False})
    logger.debug(
        f"Create task response status code: {create_task_response.status_code} and data: {create_task_response.data}"
    )
    task_id = create_task_response.get_json()["id"]

    response = client.delete(f"/tasks/{task_id}")
    logger.debug(
        f"Delete task response status code: {response.status_code} and data: {response.data}"
    )
    assert response.status_code == 200

    data = response.get_json()
    assert data["id"] == task_id
    logger.info("test_delete_task completed successfully.")


@pytest.mark.integration
def test_delete_task_commit_exception(client):
    logger.info("Starting test_delete_task_commit_exception...")
    create_task_response = client.post("/tasks", json={"title": "test", "done": False})
    logger.debug(
        f"Create task response status code: {create_task_response.status_code} and data: {create_task_response.data}"
    )
    task_id = create_task_response.get_json()["id"]

    with patch("task_api.models.task.db.session.commit") as mocked_commit:
        mocked_commit.side_effect = Exception("DB error")

        response = client.delete(f"/tasks/{task_id}")
        logger.debug(
            f"Delete task response status code: {response.status_code} and data: {response.data}"
        )
        assert response.status_code == 500
        assert b"DB error" in response.data
    logger.info("test_delete_task_commit_exception completed successfully.")


@pytest.mark.integration
def test_update_task(client):
    logger.info("Starting test_update_task...")
    create_task_response = client.post("/tasks", json={"title": "test", "done": False})
    logger.debug(
        f"Create task response status code: {create_task_response.status_code} and data: {create_task_response.data}"
    )
    task_id = create_task_response.get_json()["id"]

    response = client.patch(f"/tasks/{task_id}", json={"done": True})
    logger.debug(
        f"Update task response status code: {response.status_code} and data: {response.data}"
    )
    assert response.status_code == 200

    data = response.get_json()
    assert data["id"] == task_id and data["title"] == "test" and data["done"] is True
    logger.info("test_update_task completed successfully.")


@pytest.mark.integration
def test_update_task_without_fields(client):
    logger.info("Starting test_update_task_without_fields...")
    create_task_response = client.post("/tasks", json={"title": "test", "done": False})
    logger.debug(
        f"Create task response status code: {create_task_response.status_code} and data: {create_task_response.data}"
    )
    task_id = create_task_response.get_json()["id"]

    response = client.patch(f"/tasks/{task_id}", json={})
    logger.debug(
        f"Update task response status code: {response.status_code} and data: {response.data}"
    )
    assert response.status_code == 400
    assert b"errors" in response.data
    logger.info("test_update_task_without_fields completed successfully.")


@pytest.mark.integration
def test_update_task_commit_exception(client):
    logger.info("Starting test_update_task_commit_exception...")
    create_task_response = client.post("/tasks", json={"title": "test", "done": False})
    logger.debug(
        f"Create task response status code: {create_task_response.status_code} and data: {create_task_response.data}"
    )
    task_id = create_task_response.get_json()["id"]

    with patch("task_api.models.task.db.session.commit") as mocked_commit:
        mocked_commit.side_effect = Exception("DB error")

        response = client.patch(
            f"/tasks/{task_id}", json={"title": "Test", "done": False}
        )
        logger.debug(
            f"Update task response status code: {response.status_code} and data: {response.data}"
        )
        assert response.status_code == 500
        assert b"DB error" in response.data
    logger.info("test_update_task_commit_exception completed successfully.")
