# Household Chores - MVP

## Core Features (2-4 features for the spec)
1. **Add a task**: Any user can create a new chore task with a title and description.
2. **Assign a user**: Any user can assign an existing task to a specific member of the household.
3. **Mark as done**: The assigned user can mark the task as completed.
4. **View the list**: All users can see the full list of tasks, who is assigned to each, and the status (New / In Progress / Done).

## User Roles
- No complex authentication. Users are just names (strings) for simplicity in MVP.
- Any user can do all actions (add, assign, complete).

## Tech Stack
- Framework: Django (Python)
- Database: SQLite (default)
- Dependencies: managed with uv
- Testing: pytest
