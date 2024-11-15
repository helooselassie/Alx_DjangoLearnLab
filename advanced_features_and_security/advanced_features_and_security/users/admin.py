from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'date_of_birth', 'is_staff']
    ordering = ['email']

admin.site.register(CustomUser, CustomUserAdmin)