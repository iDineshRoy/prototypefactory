from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField

class Project(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    description = RichTextField()
    resources = models.CharField(max_length=200, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
