from django.contrib import admin
from authentication.models import User
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models


class UserAdminConfig(UserAdmin):
  model = User
  search_fields = ('email', 'user_name',)
  list_filter = ('id', 'email', 'user_name', 'is_active', 'is_staff',)
  ordering = ('-created_at',)
  list_display = ('id', 'email', 'user_name', 'is_active', 'is_staff',)
  fieldsets = (
    (None, {'fields': ('email', 'user_name', )}),
    ('Permissions', {'fields': ('is_staff', 'is_active',)}),
  )
  formfield_overrides = {
    models.TextField: {'widjet': Textarea(attrs={'rows': 20, 'cols': 60})},
  }
  add_fieldsets = (
    (None, {
      'classes': ('wide',),
      'fields': (
        'email',
        'user_name',
        'is_active',
        'is_staff',
      )
    })
  )

admin.site.register(User, UserAdminConfig)