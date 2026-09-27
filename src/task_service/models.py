from dataclasses import dataclass
from datetime import datetime

from task_service.exceptions import InvalidTaskError


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
            raise InvalidTaskError("Priority must be low, medium, or high")
