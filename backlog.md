# Development Backlog

## 1. Set up Django project and app
- **Goal**: Initialize the Django project and a dedicated app.
- **Description**: Install Django via uv, run startproject and startapp. Register the app in settings.py. Create a dummy test to verify the setup.

## 2. Create the Task model
- **Goal**: Build the database model for chores.
- **Description**: Create a Task model with fields: title, description, assigned_to, status, created_at. Run migrations.

## 3. List all tasks
- **Goal**: Create a homepage to display all tasks.
- **Description**: Write a view that fetches all tasks from the DB and renders them in a template.

## 4. Add a new task
- **Goal**: Create a form to add new tasks.
- **Description**: Build a Django ModelForm for Task. Create a view and template with a form.

## 5. Assign a user to a task
- **Goal**: Allow assigning a user to an existing task.
- **Description**: Add an "Assign" button and a simple form to update the assigned_to field.

## 6. Mark task as done
- **Goal**: Allow marking a task as completed.
- **Description**: Add a "Complete" button to update the status to "Done".
