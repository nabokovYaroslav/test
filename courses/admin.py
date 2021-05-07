from django.contrib import admin

from courses.models import Course, Lesson
from tests.models import Test
from theories.models import Theory
from homeworks.models import Homework, UserHomework, UserHomeworkAnswer, UserHomoworkAnswerReview
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Test)
admin.site.register(Theory)
admin.site.register(Homework)
admin.site.register(UserHomework)
admin.site.register(UserHomeworkAnswer)
admin.site.register(UserHomoworkAnswerReview)