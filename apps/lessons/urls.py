from django.urls import path

from apps.lessons.views import (
    CategoryListView,
    LessonListView,
    LessonDetailView,
    QuestionByLessonListView,
    SubmitAnswerView,
)
urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('lessons/', LessonListView.as_view(), name='lesson-list'),
    path('lessons/<int:pk>/', LessonDetailView.as_view(), name='lesson-detail'),
    path('lessons/<int:lesson_id>/questions/', QuestionByLessonListView.as_view(), name='question-by-lesson-list'),
    path('lessons/<int:lesson_id>/questions/<int:pk>/answer/', SubmitAnswerView.as_view(), name='submit-answer'),
]