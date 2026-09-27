from dataclasses import dataclass
from datetime import datetime


class InvalidTaskError(Exception):
    pass


@dataclass
class Task:
    id: int
    title: str
    description: str
    priority: str
    completed: bool
    reminder_at: datetime | None = None

    def __post_init__(self) -> None:
        if self.id <= 0:
            raise InvalidTaskError("Task id must be greater than 0")

        if not self.title.strip():
            raise InvalidTaskError("Task title cannot be empty")

        if self.priority not in {"low", "medium", "high"}:
            raise InvalidTaskError(
                "Priority must be low, medium, or high"
            )


def main() -> None:
    try:
        task = Task(
            id=1,
            title="Finish Week 1",
            description="Complete Python foundations",
            priority="high",
            completed=False,
            reminder_at=datetime(2026, 10, 1, 18, 30),
        )

        print(task)

    except InvalidTaskError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()