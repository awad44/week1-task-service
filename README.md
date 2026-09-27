# Week 1 Task Management Service

A small typed Python task service created as part of the NERUOS Full-Stack Software Engineering Internship Week 1 practice.

## Features

- Create typed task objects
- Validate task data
- Support task priorities
- Support optional task reminders
- Use environment variables for configuration
- Enforce formatting and linting with Black and Ruff
- Run automated quality checks with pre-commit
- Support timezone-aware task reminders

## Task Fields

Each task contains:

- `id`
- `title`
- `description`
- `priority`
- `completed`
- `reminder_at`


## Technical Decisions

- Used `dataclass` for the Task model to keep the data model simple and typed.
- Used in-memory storage for Week 1 because database persistence is outside this week's scope.
- Used timezone-aware datetime values for task reminders.
- Used `.env` for environment-specific configuration.
- Used Ruff, Black, and pre-commit to enforce code quality.
- Kept task business logic inside `TaskService` instead of `main.py`.


## Project Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd week1-task-service