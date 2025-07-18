from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum

from apps.leaderboard.models import Leaderboard
from apps.progress.models import UserProgress

@receiver(post_save, sender=UserProgress)
def update_user_progress(sender, instance, created, **kwargs):
    if created:
        total_xp = UserProgress.objects.filter(
            user=instance.user,
        ).aggregate(Sum('amount'))['amount_sum'] or 0
        
        leaderboard, _ = Leaderboard.objects.update_or_create(
            user=instance.user,
            defaults={
                'total_xp': total_xp,
            },
        )
        leaderboard.update_rank()
