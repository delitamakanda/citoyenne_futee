from django.db import models

from apps.accounts.models import CustomUser


class Leaderboard(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_xp_points = models.PositiveIntegerField(default=0)
    rank = models.PositiveIntegerField(null=True, blank=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.user.username} - Rank: {self.rank}'
    class Meta:
        verbose_name_plural = 'leaderboards'
        ordering = ['-total_xp_points']
    
    @staticmethod
    def update_rank(cls):
        leaderboard = cls.objects.all().order_by('-total_xp_points')
        for i, user in enumerate(leaderboard, start=1):
            user.rank = i
            user.save(update_fields=['rank'])