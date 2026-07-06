# pyrefly: ignore [missing-import]
from django.shortcuts import render
# pyrefly: ignore [missing-import]
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
# pyrefly: ignore [missing-import]
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    #return HttpResponse("<h2>Index Page</h2>")
    title = "Welcome to Django"
    return render(request, "index.html", {"titulo": title})

def about(request):
    username = "jorge"
    numeros = [1,2,3]
    return render(request, "about.html", {"user": username})

def hello(request, username):
    print(username)
    return HttpResponse(f"<h2>Hello {username}</h2>")

def hello2(request, id):
    print(type(id))
    result = id + 100 * 2
    return HttpResponse("<h2>Hello World %s</h2>" % result)

def projects(request):    
    #return JsonResponse({"message": projects}, safe=False)
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, "projects.html", {"projects": projects})

# def tasks(request, id):
#     task = Task.objects.get(id=id)
#     task = get_object_or_404(Task, id=id)
#     return HttpResponse(f"Task: {task.title}")

def tasks(request):
    tasks = Task.objects.all()
    return render(request, "tasks.html", {"tasks": tasks})