from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.models import Group, Permission

class CustomUser(AbstractUser, PermissionsMixin):
    bio = models.TextField(max_length=500, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_images', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=True, blank=True)      
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customer_set',
        blank=True,
    )    

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # Change this to something unique
        blank=True,
    )    
    

  
    def __str__(self):
        return self.username
    
    
    
    
    @property
    def is_staff_or_superuser(self):
        return self.is_staff or self.is_superuser
    
class User(AbstractUser):
    following = models.ManyToManyField('self', blank=True, related_name='followers')

    def __str__(self):
        return self.username    