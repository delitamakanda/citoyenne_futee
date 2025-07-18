from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django import forms

from apps.lessons.models import (
    Lesson,
Question,
Choice,
Category,
)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1
    show_change_link = True
    
    
class LessonAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget)
    class Meta:
        model = Lesson
        fields = '__all__'
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }
    
class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ('title', 'category', 'is_active')
    list_filter = ('category', 'is_active',)
    search_fields = ('title',)
    autocomplete_fields = ['category']
    form = LessonAdminForm
    fieldsets = (
        (None, {
            'fields': ('title', 'category', 'is_active')
        }),
        ('Content', {
    'fields': ('content',)
        }),
    )
    
    
class QuestionAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget)
    class Meta:
        model = Question
        fields = '__all__'
    
    
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('lesson', 'text', 'type')
    list_filter = ('type',)
    search_fields = ('text',)
    autocomplete_fields = ['lesson']
    form = QuestionAdminForm
    
    
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'text', 'is_correct')
    list_filter = ('is_correct',)
    search_fields = ('text',)
    autocomplete_fields = ['question']
    

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')
    search_fields = ('name',)

admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Category, CategoryAdmin)
