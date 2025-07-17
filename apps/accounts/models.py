from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
        ('parent', 'Parent'),
    ]
    role = models.CharField(max_length=10, choices=ROLES, default='student')
    avatar = models.CharField(max_length=255, blank=True)
