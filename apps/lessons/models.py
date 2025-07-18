from django.db import models
from ckeditor.fields import RichTextField

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.title} - {self.category.name}'
    
    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'lessons'


class Question(models.Model):
    QUESTION_TYPES = [
        ('multiple_choice', 'Multiple Choice'),
        ('true_false', 'True/False'),
        ('fill_in_the_blank', 'Fill in the Blank'),
        ('drag_and_drop', 'Drag and Drop'),
    ]
    lesson = models.ForeignKey(Lesson, related_name='question', on_delete=models.CASCADE)
    text = models.TextField()
    type = models.CharField(max_length=20, choices=QUESTION_TYPES)
    
    def __str__(self):
        return f'{self.text[:50]}...'
    
    class Meta:
        verbose_name_plural = 'questions'
        ordering = ['-id']
        unique_together = ('lesson', 'text')

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name_plural = 'choices'
        ordering = ['-id']
        unique_together = ('question', 'text')


class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['name']
        unique_together = ('name', 'icon')
