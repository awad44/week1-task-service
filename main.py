import os
from datetime import UTC, datetime

from dotenv import load_dotenv

from task_service.exceptions import InvalidTaskError
from task_service.models import Task
from task_service.service import TaskService

load_dotenv()


def main() -> None:
    app_name = os.getenv("APP_NAME", "Task Service")
    app_env = os.getenv("APP_ENV", "development")

    print(f"{app_name} - {app_env}")

    service = TaskService()

    try:
        task1 = Task(
            id=1,
            title="Finish Week 1",
            description="Complete Python foundations",
            priority="high",
            completed=False,
            reminder_at=datetime(2026, 10, 1, 18, 30, tzinfo=UTC),
        )

        task2 = Task(
            id=2,
            title="Review Git",
            description="Practice branches and pull requests",
            priority="medium",
            completed=False,
        )

        service.create_task(task1)
        service.create_task(task2)

        print("\nAll tasks:")
        print(service.get_tasks())

        print("\nTask with id 1:")
        print(service.get_task(1))

        service.complete_task(1)

        print("\nTask 1 after completion:")
        print(service.get_task(1))

        service.delete_task(2)

        print("\nTasks after deleting task 2:")
        print(service.get_tasks())

    except InvalidTaskError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
