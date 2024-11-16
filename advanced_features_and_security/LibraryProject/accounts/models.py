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
    

# models.py

from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    
    # Specify on_delete behavior for ForeignKey
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)  # Use CASCADE or another option as needed
    starter = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)  # Specify on_delete here too

    def __str__(self):
        return self.subject

class Post(models.Model):
    message = models.TextField(max_length=4000)
    
    # Specify on_delete behavior for ForeignKey
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.SET_NULL)  # Use SET_NULL or another option as needed

    def __str__(self):
        return self.message
