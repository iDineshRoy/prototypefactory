from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Project(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    description = RichTextField()
    resources = models.CharField(max_length=200, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True, related_name='user_likes')
