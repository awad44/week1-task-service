from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:
    id: int
    title: str
    description: str
    priority: str
    completed: bool
    reminder_at: datetime | None = None


def main() -> None:
    task = Task(
    id=1,
    title="Finish Week 1",
    description="Complete the internship Week 1 project",
    priority="high",
    completed=False,
    reminder_at=datetime(2026, 10, 1, 18, 30),
)

    print(task)


if __name__ == "__main__":
    main()