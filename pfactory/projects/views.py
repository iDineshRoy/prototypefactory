from django.http import HttpResponse
from django.shortcuts import render

from .models import Project
from .forms import ProjectModelForm

# Create your views here.
def homepage(request):
    return render(request, "base.html", {})

def view_project(request):
    projects = Project.objects.all().order_by('-id')[:4]
    return render(request, "projects.html", { "projects": projects })

def add_project(request):
    form = ProjectModelForm(request.POST or None)
    return render(request, "add_project.html", { "form": form })