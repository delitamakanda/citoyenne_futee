from django.db import models
from apps.accounts.models import CustomUser

class Badge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=100)
    condition = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'badges'
        ordering = ['-id']
        unique_together = ('name', 'description', 'icon', 'condition')

class UserBadge(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    earned_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user.username} - {self.badge.name}'
    class Meta:
        verbose_name_plural = 'user badges'
        unique_together = ('user', 'badge')
        ordering = ['-earned_at']

