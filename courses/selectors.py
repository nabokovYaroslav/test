from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Course, Lesson

def get_courses_list(self):
  return get_list_or_404(Course)

def get_course_detail(self):
  return get_object_or_404(Course, pk=self.kwargs['pk'])

def get_lessons_list(self):
  course = self.kwargs['pk']
  return get_list_or_404(Lesson.objects.select_related('course').select_related('homework'), course=course)

def get_lesson_detail(self):
  return get_object_or_404(Lesson.objects.select_related('course'), pk=self.kwargs['pk'], course = self.kwargs['course_pk'])