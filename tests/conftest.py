import pytest
from fastapi.testclient import TestClient
from app.services import background_tasks
from main import app
from app.models import Task


@pytest.fixture
def test_client():
    return TestClient(app)


@pytest.fixture
def database():
    task_data: list = [
        Task(**{"x": 10, "y": 5, "oper": "+"}),
        Task(**{"x": 10, "y": 5, "oper": "-"}),
        Task(**{"x": 10, "y": 5, "oper": "/"}),
        Task(**{"x": 10, "y": 5, "oper": "*"})
    ]
    for i in range(len(task_data)):
        background_tasks[i + 1] = {'status': 'waiting', 'task': task_data[i]}
    return background_tasks
