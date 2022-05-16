from django.urls import path, include
from accounts.views import (
    register, logout_view, signin, changepassword
)
from django.contrib.auth import views

urlpatterns = [
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', signin, name='login'),
    path('changepwd/', changepassword),
    
    path('reset_password/', views.PasswordResetView.as_view(template_name='password/password_reset.html'), name='reset_password'),
    path('reset_password_sent/', views.PasswordResetDoneView.as_view(template_name='password/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', views.PasswordResetConfirmView.as_view(template_name='password/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete', views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),
]