from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import Group, Permission
from rest_framework import serializers
from django.contrib.auth.models import User
from django.conf import settings
#from accounts.models import CustomUser
#from django.contrib.auth import get_user_model

#CustomUser = get_user_model()


class Follow(models.Model):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='following_accounts', on_delete=models.CASCADE)
    followed = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='followers_accounts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.follower} follows {self.followed}"

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",  # Unique related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_user_permissions",  # Unique related_name
        blank=True
    )

    class Meta:
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"

    def __str__(self):
        return self.username
    
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
        fields = ('id', 'username', 'password', 'email')  # Include necessary fields

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Hash the password
        
        user.save()
        return user    
    