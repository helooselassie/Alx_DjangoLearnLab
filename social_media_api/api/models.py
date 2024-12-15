from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=255, default='Default Title') 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts_created', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[:20]
