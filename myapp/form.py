# pyrefly: ignore [missing-import]
from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200)
    description = forms.CharField(widget=forms.Textarea, label="Descripcion", required=False)
    done = forms.BooleanField(label="¿Tarea realizada?", required=False, initial=False)

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del proyecto", max_length=200)
    #description = forms.CharField(widget=forms.Textarea, label="Descripcion", required=False)
    #url = forms.CharField(widget=forms.Textarea, label="URL", required=False)
