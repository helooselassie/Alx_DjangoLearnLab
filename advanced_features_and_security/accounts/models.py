# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager  # Ensure you have a custom user manager

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Ensure email is unique
    USERNAME_FIELD = 'email'  # Use email for authentication
    REQUIRED_FIELDS = []  # No additional fields required for superuser creation
    objects = CustomUserManager()  # Use your custom manager
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        return self.email
    


