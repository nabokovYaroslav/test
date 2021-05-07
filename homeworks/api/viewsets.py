from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from permissions.permisions import IsSubscribed, IsSubscribedOrIsAdmin
from .serializers import HomeworkSerializer, UserHomeworkSerializer, UserHomeworkAnswerSerializer, UserHomeworkAnswerReviewSerializer
from homeworks.models import Homework, UserHomework, UserHomeworkAnswer, UserHomoworkAnswerReview


class HomeworkViewSet(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticated, IsSubscribed]
  queryset = Homework.objects.all()
  serializer_class = HomeworkSerializer


class UserHomeworkViewSet(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticated, IsSubscribed]
  queryset = UserHomework.objects.all()
  serializer_class = UserHomeworkSerializer


class UserHomeworkAnswerViewSet(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticated, IsSubscribed]
  queryset = UserHomeworkAnswer.objects.all()
  serializer_class = UserHomeworkAnswerSerializer


class UserHomeworkAnswerReviewViewSet(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticated, IsSubscribed]
  queryset = UserHomoworkAnswerReview.objects.all()
  serializer_class = UserHomeworkAnswerReviewSerializer