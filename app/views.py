from fastapi import APIRouter

from app.models import Task, Tasks
from app.services import background_tasks, calculate

app = APIRouter()


@app.post('/add_task')
async def add_task(task: Task) -> dict[str, int]:
    task_id: int = len(background_tasks) + 1
    background_tasks[task_id]: dict = {'status': 'waiting', 'task': task}
    return {'task_id': task_id}


@app.get('/task/{task_id}')
async def get_task(task_id: int) -> dict[str, int | str]:
    if task_id in background_tasks:
        res: int | str = await calculate(int(task_id))
        return {'result': res}
    return {'detail': f'id: {task_id} - не найден.'}


@app.get('/tasks')
async def get_tasks() -> list[Tasks]:
    data = []
    for task_id, task_data in background_tasks.items():
        data.append(Tasks(**{'id': task_id,
                             'status': task_data['status']}))
    return data
