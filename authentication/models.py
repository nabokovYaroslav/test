from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from courses.models import Course


class UserManager(BaseUserManager):

  def create_superuser(self, email, user_name, password, **payload):

    payload.setdefault('is_staff', True)
    payload.setdefault('is_superuser', True)
    payload.setdefault('is_active', True)

    if payload.get('is_staff') is not True:
      raise ValueError('Superuser must be assigned to is_staff=True.')
    if payload.get('is_superuser') is not True:
      raise ValueError('Superuser must be assigned to is_superuser=True.')

    return self.create_user(email, user_name, password, **payload)

  def create_user(self, email, user_name, password, **payload):

    if not email:
      raise ValueError('You must provide an email address')

    if not user_name:
      raise ValueError('You must provide an username')

    email = self.normalize_email(email)
    user = self.model(email=email, user_name=user_name, **payload)
    user.set_password(password)
    user.save()
    return user


class User(AbstractBaseUser, PermissionsMixin):

  email = models.EmailField(db_index=True, unique=True)
  user_name = models.CharField(max_length=128, unique=True)
  created_at = models.DateTimeField(auto_now=True)
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  courses = models.ManyToManyField(Course)
  objects = UserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['user_name']

  def __str__(self):
      return self.user_name