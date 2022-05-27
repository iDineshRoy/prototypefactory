from django.shortcuts import get_list_or_404, render, redirect, get_object_or_404

from .models import Project
from .forms import ProjectModelForm

# Create your views here.
def homepage(request):
    return render(request, "base.html", {})

def view_projects(request):
    projects = Project.objects.all().order_by('-id')[:4]
    return render(request, "projects.html", { "projects": projects })

def view_project(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, "show_project.html", { "p": project })

def add_project(request):
    form = ProjectModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect('/')
    context = { 'form': form }
    return render(request, "add_project.html", context)

def register_interest(request, p_id):
    obj = get_object_or_404(Project, pk=p_id)
    if obj.status == "open":
        obj.status = "registered interest"
    # if obj.interests.filter(id=request.user.id).exists():
    #     obj.interests.remove(request.user)
    # else:
    #     obj.likes.add(request.user)
        obj.interests.add(request.user)
    obj.save(update_fields=["status"])
    projects = get_list_or_404(Project, pk=p_id)
    return render(request, "projects.html", { "projects": projects })

def show_profile(request, id):
    obj = Project.objects.filter(interests=request.user)
    posted_by = Project.objects.filter(user=request.user)
    interests = request.user.interests.filter(user=request.user)
    return render(request, "profile.html", { "projects": obj, "posted_by": posted_by, "interests": interests })