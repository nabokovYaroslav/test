from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Theory

def get_theories_list(self):
  return get_list_or_404(Theory.objects.select_related('lesson'), lesson=self.kwargs['lesson_pk'])

def get_theory_object(self):
  return get_object_or_404(Theory.objects.select_related('lesson'), lesson=self.kwargs['lesson_pk'], pk=self.kwargs['pk'])