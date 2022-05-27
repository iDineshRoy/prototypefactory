from django.urls import path
from .views import add_project, homepage, register_interest, show_profile, view_projects, view_project
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', homepage, name="home"),
    path('projects/', view_projects, name="show_projects"),
    path('project/<str:id>', view_project, name="show_project"),
    path('add/', add_project, name="add_project"),
    path('update/<str:p_id>', register_interest, name="register_interest"),
    path('profile/<str:id>', show_profile, name="profile"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
