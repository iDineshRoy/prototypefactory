from django.shortcuts import get_list_or_404, render, redirect, get_object_or_404

from .models import Project
from .forms import ProjectModelForm
from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.
def homepage(request):
    a = Project.objects.all().count()
    projects = Project.objects.order_by('?')[:3]
    return render(request, "base.html", { "number": a, "projects": projects })

def view_projects(request):
    obj_list = Project.objects.all().order_by('-id')
    num = len(obj_list)
    paginator = Paginator(obj_list,5)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        obj = paginator.page(page)
    except(EmptyPage, InvalidPage):
        obj = paginator.page(paginator.num_pages)
    context = {"projects":obj, "number":num}
    return render(request, "projects.html", context)

def view_project(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, "show_project.html", { "p": project })

def add_project(request):
    form = ProjectModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect('show_projects')
    context = { 'form': form }
    context["msg"] = "Project addded successfully!"
    return render(request, "add_project.html", context)

def update_project(request, id):
    project = Project.objects.get(id=id)
    form = ProjectModelForm(request.POST or None, instance=project)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect('show_project', id)
    context = { 'form': form }
    context["msg"] = "Project addded successfully!"
    return render(request, "add_project.html", context)

def register_interest(request, p_id):
    obj = get_object_or_404(Project, pk=p_id)
    if obj.status == "open" or "register_interest":
        obj.status = "registered interest"
        obj.interests.add(request.user)
    obj.save(update_fields=["status"])
    projects = get_list_or_404(Project, pk=p_id)
    return render(request, "projects.html", { "projects": projects })

def show_profile(request, id):
    obj = Project.objects.filter(interests=request.user).order_by('-id')
    posted_by = Project.objects.filter(user=request.user).order_by('-id')
    context = {}
    context["projects"] = obj
    context["posted_by"] = posted_by
    return render(request, "profile.html", context)

def approve_to_work(request, p_id):
    obj = get_object_or_404(Project, pk=p_id)
    if obj.status == "registered interest" and obj.user == request.user:
        obj.status = "approved"
    obj.save(update_fields=["status"])
    projects = get_list_or_404(Project, pk=p_id)
    return render(request, "projects.html", { "projects": projects })

def deny_to_work(request, p_id):
    obj = get_object_or_404(Project, pk=p_id)
    if obj.status == "registered interest" and obj.user == request.user:
        obj.status = "open"
    obj.save(update_fields=["status"])
    projects = get_list_or_404(Project, pk=p_id)
    return render(request, "projects.html", { "projects": projects })

def initiate_work(request, p_id):
    obj = get_object_or_404(Project, pk=p_id)
    if obj.status == "approved":
        obj.status = "work in progress"
    obj.save(update_fields=["status"])
    projects = get_list_or_404(Project, pk=p_id)
    return render(request, "projects.html", { "projects": projects })

def view_tag_industry(request, ind):
    projects = Project.objects.filter(industry=ind).distinct()[:10]
    return render(request, "projects.html", { "projects": projects })

def view_tag_company(request, comp):
    projects = Project.objects.filter(company=comp).distinct()[:10]
    return render(request, "projects.html", { "projects": projects })

def view_tag_location(request, loc):
    projects = Project.objects.filter(location=loc).distinct()[:10]
    return render(request, "projects.html", { "projects": projects })

def view_tag_technology(request, tec):
    projects = Project.objects.filter(technology=tec).distinct()[:10]
    return render(request, "projects.html", { "projects": projects })