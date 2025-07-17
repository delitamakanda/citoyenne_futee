from django.db import models

class Feedback(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    statisfaction_score = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f'Feedback #{self.id}'
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Feedbacks'
        

        
        
