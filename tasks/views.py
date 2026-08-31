from django.shortcuts import get_object_or_404, redirect, render

from .forms import AssignForm, TaskForm
from .models import Task


def task_list(request):
    tasks = Task.objects.order_by("-created_at")
    return render(request, "tasks/task_list.html", {"tasks": tasks})


def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm()
    return render(request, "tasks/task_form.html", {"form": form})


def task_assign(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = AssignForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = AssignForm(instance=task)
    return render(request, "tasks/task_assign.html", {"form": form, "task": task})


def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.status = Task.Status.DONE
        task.save()
    return redirect("task_list")
