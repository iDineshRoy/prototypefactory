from django.urls import path
from .views import add_project, approve_to_work, deny_to_work, homepage, initiate_work, register_interest, show_profile, view_projects, view_project, view_tag_industry, update_project, view_tag_company, view_tag_location, view_tag_technology
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', homepage, name="home"),
    path('projects/', view_projects, name="show_projects"),
    path('projects/industry/<str:ind>/', view_tag_industry, name="tags"),
    path('projects/company/<str:comp>/', view_tag_company, name="company"),
    path('projects/location/<str:loc>/', view_tag_location, name="location"),
    path('projects/technology/<str:tec>/', view_tag_technology, name="technology"),
    path('project/<str:id>/', view_project, name="show_project"),
    path('project/update/<str:id>/', update_project, name="update_project"),
    path('project/approve/<str:p_id>/<str:u_id>/', approve_to_work, name="approve"),
    path('project/deny/<str:p_id>/<str:u_id>/', deny_to_work, name="deny"),
    path('project/initiate/<str:p_id>/', initiate_work, name="initiate_work"),
    path('add/', add_project, name="add_project"),
    path('project/register/<str:p_id>/', register_interest, name="register_interest"),
    path('profile/<str:id>/', show_profile, name="profile"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
