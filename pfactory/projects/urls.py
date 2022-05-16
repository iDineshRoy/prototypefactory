from turtle import home
from django.urls import path, include
from .views import homepage, view_project
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', homepage, name="home"),
    path('projects/', view_project, name="show_projects"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
