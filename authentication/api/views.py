from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from .serializers import RegisterUserSerializer
from rest_framework.permissions import AllowAny
from authentication.models import User


class UserCreate(CreateAPIView):
  permission_classes = [AllowAny]
  serializer_class = RegisterUserSerializer