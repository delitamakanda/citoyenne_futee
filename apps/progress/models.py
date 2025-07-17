from django.db import models
from apps.accounts.models import CustomUser
from apps.lessons.models import Lesson


class UserProgress(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    xp_learned = models.PositiveIntegerField(default=0)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.user.username} - {self.lesson.title}'
    
    class Meta:
        verbose_name_plural = 'user progress'
        unique_together = ('user', 'lesson')
        ordering = ['-completed_at']

class Session(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    current_question = models.IntegerField(default=0)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.user.username} - {self.lesson.title}'
    
    class Meta:
        verbose_name_plural ='sessions'
        unique_together = ('user', 'lesson')
        ordering = ['-started_at']
    
