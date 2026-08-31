from django.urls import path

from . import views

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("new/", views.task_create, name="task_create"),
    path("<int:pk>/assign/", views.task_assign, name="task_assign"),
    path("<int:pk>/complete/", views.task_complete, name="task_complete"),
]
