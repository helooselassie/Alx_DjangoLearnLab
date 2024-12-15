from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.models import Group, Permission
from rest_framework import serializers
from django.contrib.auth.models import User
from django.conf import settings





class Follow(models.Model):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='following_accounts', on_delete=models.CASCADE)
    followed = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='followers_accounts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.follower} follows {self.followed}"

class CustomUser(AbstractUser, PermissionsMixin):
    bio = models.TextField(max_length=500, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_images', blank=True, null=True)
    followers = models.ManyToManyField('self', blank=True)      
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customer_set',
        blank=True,
    )  

    following = models.ManyToManyField('self', symmetrical=True, blank=True)

    def __str__(self):
        return self.username  

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
    following = models.ManyToManyField('self', symmetrical=False, blank=True)

    def __str__(self):
        return self.username    
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'bio', 'profile_picture')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Ensure this is the correct model
        fields = ('username', 'password', 'email')  # Include necessary fields

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Hash the password
        
        user.save()
        return user    