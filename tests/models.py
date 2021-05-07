from django.db import models
from django.conf import settings
from courses.models import Lesson
from datetime import datetime
import pytz

utc = pytz.UTC


class Test(models.Model):
  title = models.CharField(max_length=255)
  lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE)
  time_to_complete = models.PositiveIntegerField(default=15*60)
  start_at = models.DateTimeField()
  end_at = models.DateTimeField()

  @property
  def available(self):
    datetime_start = self.start_at.replace(tzinfo=utc)
    datetime_end = self.end_at.replace(tzinfo=utc)
    datetime_now = datetime.now().replace(tzinfo=utc)
    if(datetime_now>datetime_start and datetime_now<datetime_end):
      return True
    return False

  def __str__(self):
    return self.title


class Question(models.Model):
  types = (
    ("radio", "radio"),
    ("checkbox", "checkbox"),
    ("text", "text"),
  )
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  test = models.ForeignKey(Test, on_delete=models.CASCADE)
  type = models.CharField(max_length=20, choices=types, default="radio")
  points = models.PositiveIntegerField()

  def __str__(self):
    return self.title
  

class AnswerOption(models.Model):
  option = models.CharField(max_length=255)
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  is_correct = models.BooleanField()

  def __str__(self):
    return self.option


class UserTest(models.Model):
  test = models.ForeignKey(Test, on_delete=models.CASCADE)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  result = models.PositiveIntegerField(default=0)
  user_started_at = models.DateTimeField(null=True)
  user_finished_at = models.DateTimeField(null=True)

  @property
  def status(self):
    if(self.user_started_at is None):
      return 'notOpened'
    if(self.user_started_at is not None and self.user_finished_at is None):
      return 'inProccess'
    return 'finished'



class UserTestQuestionAnswer(models.Model):
  user_test = models.ForeignKey(UserTest, on_delete=models.CASCADE)
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  answer = models.ForeignKey(AnswerOption, on_delete=models.CASCADE)