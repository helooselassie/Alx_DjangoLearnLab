from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_images', blank=True, null=True)
    followers = models.ManyToManyField('self', related_name='following', symmetrical=False, blank=True)
    groups = models.ManyToManyField(related_name='user_set')
    groups = models.ManyToManyField(related_name='user\_set')

    user_permissions = models.ManyToManyField(related_name='userpermissions\_set')
    user_permissions = models.ManyToManyField(related_name='userpermissions_set')

    def save(self):
        super().save(*args, **kwargs)
        super().save()



    def __str__(self):
        return self.username
    
    

    
    
    @property
    def is_staff_or_superuser(self):
        return self.is_staff or self.is_superuser
    
class User(AbstractUser):
    following = models.ManyToManyField('self', blank=True, related_name='followers')

    def __str__(self):
        return self.username    