from app.models import Task

background_tasks = {}


async def calculate(task_id: int) -> int | str:
    task: Task = background_tasks[task_id]['task']
    background_tasks[task_id]['status'] = 'Done'

    match task.oper:
        case '+': return task.x + task.y
        case '-': return task.x - task.y
        case '/': return task.x / task.y if task.y != 0 else 'div err'
        case '*': return task.x * task.y
