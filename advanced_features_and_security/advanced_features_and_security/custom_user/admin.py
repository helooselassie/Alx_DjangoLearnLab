from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'date_of_birth', 'is_staff']
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)