from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_student = models.BooleanField('student', default=False)
    is_client = models.BooleanField('client', default=False)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    education = models.CharField(max_length=90, blank=True, null=True)
    specialization = models.CharField(max_length=50, blank=True, null=True)
    university = models.CharField(max_length=120, blank=True, null=True)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)