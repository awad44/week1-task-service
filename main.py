from datetime import UTC, datetime
import os
from dotenv import load_dotenv

from task_service.exceptions import InvalidTaskError
from task_service.models import Task

load_dotenv()


def main() -> None:
    app_name = os.getenv("APP_NAME", "Task Service")
    app_env = os.getenv("APP_ENV", "development")

    print(f"{app_name} - {app_env}")

    try:
        task = Task(
            id=1,
            title="Finish Week 1",
            description="Complete Python foundations",
            priority="high",
            completed=False,
            reminder_at=datetime(2026, 10, 1, 18, 30, tzinfo=UTC),
        )

        print("Created task:")
        print(task)

    except InvalidTaskError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
