from datetime import UTC, datetime

from task_service.exceptions import InvalidTaskError
from task_service.models import Task


def main() -> None:
    try:
        task = Task(
            id=1,
            title="Finish Week 1",
            description="Complete Python foundations",
            priority="high",
            completed=False,
            reminder_at=datetime(2026, 10, 1, 18, 30, tzinfo=UTC),
        )

        print(task)

    except InvalidTaskError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
