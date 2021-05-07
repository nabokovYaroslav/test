from rest_framework.serializers import ModelSerializer
from authentication.models import User


class RegisterUserSerializer(ModelSerializer):

  class Meta:
    model = User
    fields = ('email', 'user_name', 'password')
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):

    user = self.Meta.model(
      email = validated_data['email'],
      user_name = validated_data['user_name']
    )
    if validated_data['password'] is not None:
      user.set_password(validated_data['password'])
    user.save()
    return user


class UserSerilizer(ModelSerializer):

  class Meta:
    model = User
    fields = '__all__'
    