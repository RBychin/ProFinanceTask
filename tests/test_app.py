import asyncio
from http import HTTPStatus

from httpx import Response
from app.services import calculate


def test_add_task(test_client, database):
    """Тест добавления задачи методом POST и получения ответа."""

    count: int = len(database)
    task_data: dict = {"x": 1, "y": 1, "oper": "+"}
    response: Response = test_client.post('/add_task', json=task_data)
    assert response.status_code == HTTPStatus.OK
    result: dict = response.json()
    assert "task_id" in result
    assert isinstance(result['task_id'], int)
    assert count + 1 == len(database)
    assert response.json().get('task_id') == count + 1


def test_get_task(test_client, database):
    """Получение объекта модели Task по id методом GET."""

    response = test_client.get('/task/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'result': 15}


def test_get_tasks(test_client, database):
    """Получение списка объектов Tasks и проверка на наличие полей."""

    response = test_client.get('/tasks')
    assert response.status_code == HTTPStatus.OK
    for task_id, task in enumerate(response.json()):
        assert task['id'] == task_id + 1


def test_status_change(test_client):
    """Проверка изменения статуса после просмотра результата."""

    response: Response = test_client.get('/task/5')
    assert response.json().get('result') == 2
    response: Response = test_client.get('/tasks')
    assert response.json()[4]['status'] == 'Done'


def test_except_wrong_input(test_client):
    """Проверка валидации."""

    data = {'x': 2, 'y': 2, 'oper': '%'}
    response: Response = test_client.post('/add_task', json=data)
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_calculate_foo(database):
    """Тест функции калькуляции."""

    for task_id in database:
        res = asyncio.run(calculate(task_id))
        match task_id:
            case 1: assert res == 15
            case 2: assert res == 5
            case 3: assert res == 2.0
            case 4: assert res == 50
            case 5: assert res == 2
