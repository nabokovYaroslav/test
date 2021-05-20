from django.shortcuts import get_list_or_404, get_object_or_404
from .models import UserTest

def get_tests_list():
  return get_list_or_404(UserTest.objects.all())