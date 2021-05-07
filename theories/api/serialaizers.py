from rest_framework import serializers
from theories.models import Theory


class TheorySerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Theory
    fields = ['id', 'text', 'lesson']