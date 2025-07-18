from rest_framework import serializers
from apps.lessons.models import (
    Lesson,
    Question,
    Choice,
    Category,
)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'icon')
        read_only_fields = ('id',)


class LessonSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Lesson
        fields = ('id', 'title', 'content', 'category', 'is_active')
        read_only_fields = ('id',)
        depth = 1


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'text', 'is_correct',)
        depth = 1


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)
    class Meta:
        model = Question
        fields = ('id', 'text', 'type', 'lesson', 'choices')
        read_only_fields = ('id',)
        
class SubmitAnswserSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    anwser = serializers.CharField()
