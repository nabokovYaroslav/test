from django.db import models
from courses.models import Lesson


class Theory(models.Model):
  text = models.TextField(null=True)
  lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE)