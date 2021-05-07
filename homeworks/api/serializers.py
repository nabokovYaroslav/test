from rest_framework import serializers
from homeworks.models import Homework, UserHomework, UserHomeworkAnswer, UserHomoworkAnswerReview


class HomeworkSerializer(serializers.ModelSerializer):

  class Meta:
    model = Homework
    fields = '__all__'


class UserHomeworkSerializer(serializers.ModelSerializer):

  class Meta:
    model = UserHomework
    fields = '__all__'


class UserHomeworkAnswerSerializer(serializers.ModelSerializer):

  class Meta:
    model = UserHomeworkAnswer
    fields = '__all__'


class UserHomeworkAnswerReviewSerializer(serializers.ModelSerializer):

  class Meta:
    model = UserHomoworkAnswerReview
    fields = '__all__'