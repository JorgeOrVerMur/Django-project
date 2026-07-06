# pyrefly: ignore [missing-import]
from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.index),
    path("about/", views.about),
    path("hello/<str:username>/", views.hello),
    path("hello2/<int:id>/", views.hello2),
    path("projects/", views.projects),
    #path("tasks/<int:id>", views.tasks),
    path("tasks/", views.tasks),
]