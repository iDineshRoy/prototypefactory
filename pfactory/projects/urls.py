from django.urls import path
from .views import add_project, homepage, view_project
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', homepage, name="home"),
    path('projects/', view_project, name="show_projects"),
    path('add/', add_project, name="add_project"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
