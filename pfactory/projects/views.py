from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, "base.html", {})

def view_project(request):
    return render(request, "projects.html", {})