from django.urls import path
from .views import add_project, approve_to_work, deny_to_work, homepage, initiate_work, register_interest, show_profile, view_projects, view_project, view_tag_industry
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', homepage, name="home"),
    path('projects/', view_projects, name="show_projects"),
    path('projects/tag/<str:ind>', view_tag_industry, name="tags"),
    path('project/<str:id>/', view_project, name="show_project"),
    path('project/approve/<str:p_id>/', approve_to_work, name="approve"),
    path('project/deny/<str:p_id>/', deny_to_work, name="deny"),
    path('project/initiate/<str:p_id>/', initiate_work, name="initiate_work"),
    path('add/', add_project, name="add_project"),
    path('update/<str:p_id>/', register_interest, name="register_interest"),
    path('profile/<str:id>/', show_profile, name="profile"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
