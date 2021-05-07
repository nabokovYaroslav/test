from django.db import models
from courses.models import Lesson
from django.conf import settings

def rename_file(instance, filename):
  file_name = md5(str(time.time()).encode()).hexdigest()
  file_type = filename.split('.')[-1]
  return 'homeworks_files/{}.{}'.format(filename, file_type)

class Homework(models.Model):
  lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
  title = models.CharField(max_length=255)
  description = models.TextField()
  start_at = models.DateTimeField()
  end_at = models.DateTimeField()

  def __str__(self):
      return self.title


class UserHomework(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  homework = models.OneToOneField(Homework, on_delete=models.CASCADE)
  result = models.PositiveIntegerField(default=0)


class UserHomeworkAnswer(models.Model):
  user_homework = models.OneToOneField(UserHomework, on_delete=models.CASCADE)
  file = models.FileField(upload_to=rename_file)

class UserHomoworkAnswerReview(models.Model):
  result = models.PositiveIntegerField(default=0)
  review_description = models.TextField(null=True)
  user_homework_answer = models.OneToOneField(UserHomeworkAnswer, on_delete=models.CASCADE)