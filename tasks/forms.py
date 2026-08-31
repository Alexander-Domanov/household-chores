from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    """Form to create a new task."""

    class Meta:
        model = Task
        fields = ["title", "description"]


class AssignForm(forms.ModelForm):
    """Form to assign a user to an existing task."""

    class Meta:
        model = Task
        fields = ["assigned_to"]
        labels = {"assigned_to": "Assign to"}
