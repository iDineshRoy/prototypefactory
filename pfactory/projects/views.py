from django.shortcuts import get_list_or_404, render, redirect, get_object_or_404

from .models import Project, ProjectStatus
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
    context["projects_status"] = get_list_or_404(ProjectStatus)
    return render(request, "projects.html", context)

def view_project(request, id):
    project = get_object_or_404(Project, id=id)
    try:
        projects_status = ProjectStatus.objects.get(project=project, user=request.user)
    except:
        projects_status = False
    return render(request, "show_project.html", { "p": project, "projects_status": projects_status})

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
    try:
        obj_status = ProjectStatus.objects.create(project=obj, user=request.user, status="registered interest")
        print(obj_status.id)
    except:
        msg = "Registering interest failed!"
    try:
        projects_status = ProjectStatus.objects.get(project=obj, user=request.user)
    except:
        projects_status = False
    return render(request, "show_project.html", { "p": obj,"projects_status": projects_status })

def show_profile(request, id):
    posted_by = Project.objects.filter(user=request.user).order_by('-id')
    context = {}
    context["projects"] = ProjectStatus.objects.filter(user=request.user).order_by('-id')
    context["projects_status"] = ProjectStatus.objects.all()
    context["posted_by"] = posted_by
    return render(request, "profile.html", context)

def approve_to_work(request, p_id, u_id):
    obj = get_object_or_404(ProjectStatus, project_id=p_id, user_id=u_id)
    if obj.status == "registered interest":
        obj.status = "approved"
    obj.save(update_fields=["status"])
    context = {}
    context["projects"] = get_list_or_404(Project, pk=p_id)
    context["projects_status"] = get_list_or_404(ProjectStatus)
    context["posted_by"] = Project.objects.filter(user=request.user).order_by('-id')
    return render(request, "profile.html", context)

def deny_to_work(request, p_id, u_id):
    obj = get_object_or_404(ProjectStatus, project_id=p_id, user_id=u_id)
    if obj.status == "registered interest":
        obj.status = "denied"
    obj.save(update_fields=["status"])
    context = {}
    context["projects"] = get_list_or_404(Project, pk=p_id)
    context["projects_status"] = get_list_or_404(ProjectStatus)
    context["posted_by"] = Project.objects.filter(user=request.user).order_by('-id')
    return render(request, "profile.html", context)

def initiate_work(request, p_id):
    obj = get_object_or_404(ProjectStatus, project_id=p_id, user=request.user)
    if obj.status == "approved":
        obj.status = "work in progress"
    obj.save(update_fields=["status"])
    context = {}
    context["projects"] = ProjectStatus.objects.filter(user=request.user).order_by('-id')
    context["projects_status"] = ProjectStatus.objects.all()
    context["posted_by"] = Project.objects.filter(user=request.user).order_by('-id')
    return render(request, "profile.html", context)

def view_tag_industry(request, ind):
    projects = Project.objects.filter(industry=ind).order_by('-id').distinct()[:10]
    projects_status = get_list_or_404(ProjectStatus)
    return render(request, "projects.html", { "projects": projects,"projects_status": projects_status })

def view_tag_company(request, comp):
    projects = Project.objects.filter(company=comp).order_by('-id').distinct()[:10]
    projects_status = get_list_or_404(ProjectStatus)
    return render(request, "projects.html", { "projects": projects,"projects_status": projects_status })

def view_tag_location(request, loc):
    projects = Project.objects.filter(location=loc).order_by('-id').distinct()[:10]
    projects_status = get_list_or_404(ProjectStatus)
    return render(request, "projects.html", { "projects": projects,"projects_status": projects_status })

def view_tag_technology(request, tec):
    projects = Project.objects.filter(technology=tec).order_by('-id').distinct()[:10]
    projects_status = get_list_or_404(ProjectStatus)
    return render(request, "projects.html", { "projects": projects,"projects_status": projects_status })

def footer_content():
    projects = Project.objects.order_by('?')[:3]
    return projects