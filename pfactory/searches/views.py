from django.shortcuts import render, get_list_or_404
from django.db.models import Q
import functools, operator
from django.core.paginator import Paginator, EmptyPage, InvalidPage

from projects.models import Project, ProjectStatus
# Create your views here.
def search_view(request):
    try:
        query = request.GET.get('q', '')
        queries = request.GET.get('q', '').split()
        if query is not None:
            qset_and = functools.reduce(operator.__and__, [
                Q(industry__icontains=q) | 
                Q(company__icontains=q) |
                Q(description__icontains=q) | 
                Q(title__icontains=q) | 
                Q(technology__icontains=q) |
                Q(location__icontains=q) |
                Q(timestamp__icontains=q) |
                Q(user__first_name__icontains=q) |
                Q(user__last_name__icontains=q) 
                for q in queries])
            qset_or = functools.reduce(operator.or_, [
                Q(industry__icontains=q) | 
                Q(company__icontains=q) |
                Q(description__icontains=q) | 
                Q(title__icontains=q) | 
                Q(technology__icontains=q) |
                Q(location__icontains=q) |
                Q(timestamp__icontains=q) |
                Q(user__first_name__icontains=q) |
                Q(user__last_name__icontains=q) 
                for q in queries])
            obj_list = []
            obj_list.extend(list(Project.objects.filter(qset_and).order_by('-id')))
            obj_list.extend(list(Project.objects.filter(qset_or).order_by('-id')))
            obj_list = list(dict.fromkeys(obj_list))
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
            
            context = {"query":query, "projects":obj, "number":num }
            context["projects_status"] = get_list_or_404(ProjectStatus)
        return render(request,'projects.html', context)
    except:
        return render(request, 'pages/message.html', {'message':"Error occured!"})