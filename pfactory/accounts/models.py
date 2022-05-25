from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_student = models.BooleanField('student', default=False)
    is_client = models.BooleanField('client', default=False)