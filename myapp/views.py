# pyrefly: ignore [missing-import]
from django.shortcuts import render
# pyrefly: ignore [missing-import]
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h2>Index Page</h2>")

def hello(request, username):
    print(username)
    return HttpResponse(f"<h2>Hello {username}</h2>")

def hello2(request, id):
    print(type(id))
    result = id + 100 * 2
    return HttpResponse("<h2>Hello World %s</h2>" % result)

def about(request):
    return HttpResponse("<h2>About Page</h2>")