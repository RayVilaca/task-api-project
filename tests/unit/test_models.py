import pytest
from task_api.models.task import Task
from task_api.models.activity import Activity


@pytest.mark.unit
def test_set_title():
    task = Task(title="study", done=False)
    task.set_title("exercise")
    assert task.title == "exercise"


@pytest.mark.unit
def test_set_done():
    task = Task(title="study", done=False)
    task.set_done(True)
    assert task.done is True


@pytest.mark.unit
def test_to_dict():
    task = Task(title="study", done=False)
    assert task.to_dict() == {"id": None, "title": "study", "done": False}


@pytest.mark.unit
def test_activity_set_title():
    task = Activity(title="study", done=False)
    task.set_title("exercise")
    assert task.title == "exercise"


@pytest.mark.unit
def test_activity_set_done():
    task = Activity(title="study", done=False)
    task.set_done(True)
    assert task.done is True


@pytest.mark.unit
def test_activity_to_dict():
    task = Activity(title="study", done=False)
    assert task.to_dict() == {"id": None, "title": "study", "done": False}
