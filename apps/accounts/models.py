from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class CustomUser(AbstractUser):
    ROLES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
        ('parent', 'Parent'),
    ]
    role = models.CharField(max_length=10, choices=ROLES, default='student')
    avatar = models.CharField(max_length=255, blank=True)
    groups = models.ManyToManyField(
        Group,
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="customuser_set",
        related_query_name="customuser",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
        related_name="customuser_set",
        related_query_name="customuser",
    )
