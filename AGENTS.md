# AGENTS.md

## Commands

- `uv sync` - install dependencies
- `uv run pytest` - the whole suite
- `uv run pytest tasks/test_tasks.py` - one test file
- `uv run python manage.py runserver` - development server
- `uv run python manage.py makemigrations` / `migrate` - database changes

## Rules

- Dependencies are added in `pyproject.toml`. Do not add one without asking.
- Read the acceptance criteria before starting and before closing a task.
- Commit regularly, after each meaningful step.

## Documents

- `_docs/plan.md` - product specification
- `backlog.md` - task backlog (the only active backlog)
- `_docs/process.md` - how work is organized
- `_docs/task-template.md` - template for groomed tasks
- `_docs/team/pm.md` - product manager role
- `_docs/team/software-engineer.md` - software engineer role
- `_docs/team/qa-engineer.md` - QA engineer role
