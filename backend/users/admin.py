from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import Follow

User = get_user_model()


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'following')
    list_filter = ['user', 'following']


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    list_display = ('pk', 'username', 'email', 'first_name',
                    'last_name', 'is_staff')
    list_filter = ['email', 'username']
