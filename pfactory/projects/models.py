from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
# from django.contrib.auth import get_user_model as User
from accounts.models import User

class Project(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    description = RichTextField()
    resources = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=50, null=True, default="open")
    timestamp = models.DateTimeField(auto_now_add=True)
    interests = models.ManyToManyField(User, related_name="interests")