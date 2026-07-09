# pyrefly: ignore [missing-import]
from django.shortcuts import render
# pyrefly: ignore [missing-import]
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
# pyrefly: ignore [missing-import]
from django.shortcuts import get_object_or_404, redirect
from .form import CreateNewTask, CreateNewProject

# Create your views here.
def index(request):
    #return HttpResponse("<h2>Index Page</h2>")
    title = "Welcome to Django from Views.py"
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
    return render(request, "projects/projects.html", {"projects": projects})

# def tasks(request, id):
#     task = Task.objects.get(id=id)
#     task = get_object_or_404(Task, id=id)
#     return HttpResponse(f"Task: {task.title}")

def tasks(request):
    tasks = Task.objects.all()
    return render(request, "tasks/tasks.html", {"tasks": tasks})

def create_task(request):
    # print(request.GET["title"])
    # print(request.GET["description"])
    # print(request.GET["done"])
    #crea la tarea a partir de la peticion get
    if request.method == "GET":
        #show interface
        return render(request, "tasks/create_task.html", {"formulario": CreateNewTask()})
    else:
        done_value = 'done' in request.POST
        Task.objects.create(title=request.POST["title"], description=request.POST["description"], done=done_value, project = Project.objects.first())
        #return redirect("/myapp/tasks") #esto es lo mismo que la siguiente linea, pero usando el nombre de la ruta, se recomienda usar el nombre de la ruta
        return redirect("tasks_lista")

def create_project(request):
    if request.method == "GET":
        #show interface
        return render(request, "projects/create_project.html", {"formularioP": CreateNewProject()})
    else:
        print(request.POST) 
        name = request.POST["name"]
        project = Project.objects.create(name=name)
        print(project)
        #return redirect("/myapp/projects")
        return redirect("projects_lista")
