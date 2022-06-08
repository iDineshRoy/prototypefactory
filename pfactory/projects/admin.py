from django.contrib import admin
from .models import Project, ProjectStatus
# Register your models here.

admin.site.register(Project)
admin.site.register(ProjectStatus)