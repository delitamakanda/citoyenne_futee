import datetime

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView

from apps.lessons.models import (
    Lesson,
    Question,
    Category, Choice,
)
from apps.lessons.serializers import (
    CategorySerializer,
    LessonSerializer,
    QuestionSerializer,
    SubmitAnswserSerializer,
)
from apps.progress.models import UserProgress


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny,]
    def get_queryset(self):
        return Category.objects.filter(is_active=True)
    
    def get_serializer_context(self):
        return {'request': self.request}
    


class LessonListView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [AllowAny,]
    def get_queryset(self):
        return Lesson.objects.filter(is_active=True)
    
    def get_serializer_context(self):
        return {'request': self.request}
    

class LessonDetailView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [AllowAny,]
    def get_serializer_context(self):
        return {'request': self.request}
    def get_object(self):
        return Lesson.objects.get(id=self.kwargs['pk'], is_active=True)


class QuestionByLessonListView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny,]
    def get_serializer_context(self):
        return {'request': self.request}
    def get_object(self):
        return Question.objects.get(lesson_id=self.kwargs['lesson_id'], id=self.kwargs['pk'])
    def get_queryset(self):
        return Question.objects.filter(lesson_id=self.kwargs['lesson_id'])
    
class SubmitAnswerView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SubmitAnswserSerializer
    
    @staticmethod
    def post(self, request, *args, **kwargs):
        question_id = Question.objects.get(id=kwargs['question_id'])
        answer_data = request.data.get('answer')
        
        try:
            question = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            return Response({'error': 'Question not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if question.type == 'multiple_choice':
            return self.handle_multiple_choice(request.user, question, answer_data)
        elif question.type == 'true_false':
            return self.handle_true_false(request.user, question, answer_data)
        elif question.type == 'fill_in_the_blank':
            return self.handle_fill_in_the_blank(request.user, question, answer_data)
        elif question.type == 'drag_and_drop':
            return self.handle_drag_and_drop(request.user, question, answer_data)
        else:
            return Response({'error': 'Invalid question type'}, status=status.HTTP_400_BAD_REQUEST)
        
        
    def handle_multiple_choice(self, user, question, answer_data):
        try:
            choice_ids = Choice.objects.filter(question=question, is_correct=True)
            selected_choices = Choice.objects.filter(id__in=answer_data, question=question)
            
            is_correct = (set(selected_choices) == set(choice_ids))
            
            self.record_progress(user, question, is_correct)
            return Response({'is_correct': is_correct, 'correct_choices': list(choice_ids.values_list('id', flat=True))}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def handle_true_false(self, user, question, answer_data):
        # Implement logic to handle true/false questions
        try:
            correct_choice = Choice.objects.get(question=question, is_correct=True)
            is_correct = (answer_data.lower() == correct_choice.text.lower())
            self.record_progress(user, question, is_correct)
            return Response({'is_correct': is_correct, 'correct_choice': correct_choice.text}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    def handle_fill_in_the_blank(self, user, question, answer_data):
       try:
           correct_answers = Choice.objects.filter(question=question, is_correct=True)
           is_correct = any(
               answser.lower().strip() == answer_data.lower().strip()
               for answser in correct_answers.values_list('text', flat=True)
           )
           self.record_progress(user, question, is_correct)
           return Response({'is_correct': is_correct, 'correct_answers': list(correct_answers.values_list('text', flat=True))}, status=status.HTTP_200_OK)
       except Exception as e:
           return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    def handle_drag_and_drop(self, user, question, answer_data):
       try:
           correct_order = list(Choice.objects.filter(question=question).order_by('id').values_list('id', flat=True))
           user_order = list(answer_data.values())
           is_correct = (correct_order == user_order)
           self.record_progress(user, question, is_correct)
           return Response({'is_correct': is_correct, 'correct_order': correct_order}, status=status.HTTP_200_OK)
       except Exception as e:
           return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    @staticmethod
    def record_progress(self, user, question, is_correct):
        user_progress, created = UserProgress.objects.get_or_create(
            user=user,
            lesson=question.lesson,
            defaults={
                'completed': False,
            },
        )
        if not created:
            user_progress.save()

        if is_correct:
            base_xp = 5
            question_type_bonus = {
                'true_false': 1,
                'fill_in_the_blank': 2,
                'drag_and_drop': 3,
                'multiple_choice': 4,
            }
            xp_to_award = base_xp + question_type_bonus.get(question.type, 0)
            user_progress.xp_learned += xp_to_award
            user_progress.save()
        
        return user_progress
    
