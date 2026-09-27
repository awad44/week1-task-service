# Week 1 Task Service

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

## Project Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd week1-task-service