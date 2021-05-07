from rest_framework import serializers
from tests.models import Test, Question, AnswerOption, UserTest, UserTestQuestionAnswer
from authentication.api.serializers import UserSerilizer


class TestSerializer(serializers.ModelSerializer):

  class Meta:
    model = Test
    fields = ['title', 'lesson', 'time_to_complete', 'start_at', 'end_at']


class QuestionSerializer(serializers.ModelSerializer):
  test = TestSerializer(read_only=True)

  class Meta:
    model = Question
    fields = ['title', 'description', 'test', 'type', 'points']


class AnswerOptionSerializer(serializers.ModelSerializer):
  question = QuestionSerializer(read_only=True)

  class Meta:
    model = AnswerOption
    fields = ['option', 'question', 'is_correct']

class UserTestSerializer(serializers.ModelSerializer):
  user = UserSerilizer(read_only=True)
  test = TestSerializer(read_only=True)
  class Meta:
    model = UserTest
    fields = ['test', 'user', 'result', 'user_started_at', 'user_finished_at', 'status']

class UserTestAnswerOptionSerializer(serializers.ModelSerializer):
  user_test = UserTestSerializer(read_only=True)
  class Meta:
    model = UserTestQuestionAnswer
    fields = ['user_test', 'question', 'answer']