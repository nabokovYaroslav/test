from django.db import models
from datetime import datetime 
import pytz
utc = pytz.UTC

class Course(models.Model):
  title = models.CharField(max_length=255, unique=True)
  description = models.TextField(null=True)
  start_at = models.DateTimeField()

  @property
  def available(self):
    datetime_start = self.start_at.replace(tzinfo=utc)
    datetime_now = datetime.now().replace(tzinfo=utc)
    if(datetime_now>datetime_start):
      return False
    return True


  def __str__(self):
      return self.title
  

class Lesson(models.Model):
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  course = models.ForeignKey(Course, on_delete=models.CASCADE)

  
  def __str__(self):
      return self.title
  
