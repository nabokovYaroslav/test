from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import TestSerializer, QuestionSerializer, AnswerOptionSerializer, UserTestSerializer, UserTestAnswerOptionSerializer
from tests.models import Test, Question, AnswerOption, UserTest, UserTestQuestionAnswer
from permissions.permisions import IsSubscribed, IsSubscribedOrIsAdmin


class TestViewSet(viewsets.ModelViewSet):

  serializer_class = TestSerializer
  queryset = Test.objects.all()
  permission_classes = [IsAuthenticated, IsSubscribedOrIsAdmin]


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticated, IsSubscribedOrIsAdmin]


class AnswerOptionViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerOptionSerializer
    queryset = AnswerOption.objects.all()
    permission_classes = [IsAuthenticated, IsSubscribedOrIsAdmin]


class UserTestViewSet(viewsets.ModelViewSet):
    serializer_class = UserTestSerializer
    queryset = UserTest.objects.all()
    permission_classes = [IsAuthenticated, IsSubscribedOrIsAdmin]


class AnswerOptionViewSet(viewsets.ModelViewSet):
    serializer_class = UserTestAnswerOptionSerializer
    queryset = UserTestQuestionAnswer.objects.all()
    permission_classes = [IsAuthenticated, IsSubscribedOrIsAdmin]