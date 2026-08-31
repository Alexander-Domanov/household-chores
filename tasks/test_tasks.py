import pytest
from django.urls import reverse

from .models import Task

pytestmark = pytest.mark.django_db


def test_task_created_with_default_status():
    task = Task.objects.create(title="Wash dishes", description="Kitchen only")
    assert task.status == Task.Status.NEW
    assert task.created_at is not None
    assert str(task) == "Wash dishes"


def test_list_empty(client):
    response = client.get(reverse("task_list"))
    assert response.status_code == 200
    assert "No tasks yet" in response.content.decode()


def test_create_task(client):
    response = client.post(
        reverse("task_create"),
        {"title": "Take out trash", "description": ""},
    )
    assert response.status_code == 302
    assert Task.objects.filter(title="Take out trash").exists()


def test_list_shows_tasks(client):
    Task.objects.create(title="Mow lawn")
    response = client.get(reverse("task_list"))
    assert "Mow lawn" in response.content.decode()


def test_assign_task(client):
    task = Task.objects.create(title="Clean bathroom")
    response = client.post(
        reverse("task_assign", args=[task.pk]),
        {"assigned_to": "Anna"},
    )
    assert response.status_code == 302
    task.refresh_from_db()
    assert task.assigned_to == "Anna"


def test_complete_task(client):
    task = Task.objects.create(title="Do laundry")
    response = client.post(reverse("task_complete", args=[task.pk]))
    assert response.status_code == 302
    task.refresh_from_db()
    assert task.status == Task.Status.DONE
