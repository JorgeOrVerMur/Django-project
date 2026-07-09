# pyrefly: ignore [missing-import]
from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("hello/<str:username>/", views.hello, name="hello"),
    path("hello2/<int:id>/", views.hello2, name="hello2"),
    path("projects/", views.projects, name="projects_lista"),
    #path("tasks/<int:id>", views.tasks),
    path("tasks/", views.tasks, name="tasks_lista"),
    path("tasks/create/", views.create_task, name="create_task"),
    path("projects/create/", views.create_project, name="create_project"),
]