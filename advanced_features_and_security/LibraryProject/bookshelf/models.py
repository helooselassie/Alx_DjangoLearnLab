# LibraryProject/bookshelf/models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"


class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name
    
# bookshelf/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)  # Optional field for date of birth
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)  # Optional field for profile photo
    
    objects = CustomUserManager()

    def __str__(self):
        return self.email  # Assuming you want to use email as the identifier
    
from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)

    # Specify on_delete behavior for ForeignKey
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)  # Use CASCADE or another option as needed
    starter = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)  # Specify on_delete here too

class Post(models.Model):
    message = models.TextField(max_length=4000)

    # Specify on_delete behavior for ForeignKey
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)

    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.SET_NULL)  # Use SET_NULL or another option as needed
