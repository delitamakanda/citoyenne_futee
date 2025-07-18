from django.apps import AppConfig


class LeaderboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.leaderboard'
    
    def ready(self):
        import apps.leaderboard.signals  # noqa
