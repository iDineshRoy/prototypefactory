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
    context["msg"] = "Project addded successfully!"
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
    # client = get_object_or_404(Project, interests=request.user)
    # interests = client.interests.all()
    # print(interests)
    context = {}
    context["projects"] = obj
    context["posted_by"] = posted_by
    # context["interests"] = interests
    return render(request, "profile.html", context)

def approve_to_work(request, p_id):
    obj = get_object_or_404(Project, pk=p_id)
    if obj.status == "registered interest" and obj.user == request.user:
        obj.status = "approved"
    # if obj.interests.filter(id=request.user.id).exists():
    #     obj.interests.remove(request.user)
    # else:
    #     obj.likes.add(request.user)
        obj.interests.add(request.user)
    obj.save(update_fields=["status"])
    projects = get_list_or_404(Project, pk=p_id)
    return render(request, "projects.html", { "projects": projects })

def deny_to_work(request, p_id):
    obj = get_object_or_404(Project, pk=p_id)
    if obj.status == "registered interest" and obj.user == request.user:
        obj.status = "open"
    # if obj.interests.filter(id=request.user.id).exists():
    #     obj.interests.remove(request.user)
    # else:
    #     obj.likes.add(request.user)
        obj.interests.add(request.user)
    obj.save(update_fields=["status"])
    projects = get_list_or_404(Project, pk=p_id)
    return render(request, "projects.html", { "projects": projects })