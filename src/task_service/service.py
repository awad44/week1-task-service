from task_service.exceptions import InvalidTaskError
from task_service.models import Task


class TaskService:
    def __init__(self) -> None:
        self._tasks: list[Task] = []

    def create_task(self, task: Task) -> Task:
        if self.get_task(task.id) is not None:
            raise InvalidTaskError(f"Task with id {task.id} already exists")

        self._tasks.append(task)
        return task

    def get_tasks(self) -> list[Task]:
        return self._tasks.copy()

    def get_task(self, task_id: int) -> Task | None:
        for task in self._tasks:
            if task.id == task_id:
                return task

        return None

    def complete_task(self, task_id: int) -> Task:
        task = self.get_task(task_id)

        if task is None:
            raise InvalidTaskError(f"Task with id {task_id} was not found")

        task.completed = True
        return task

    def delete_task(self, task_id: int) -> None:
        task = self.get_task(task_id)

        if task is None:
            raise InvalidTaskError(f"Task with id {task_id} was not found")

        self._tasks.remove(task)
