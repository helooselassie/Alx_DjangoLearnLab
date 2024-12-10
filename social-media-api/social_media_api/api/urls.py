from django.urls import path
from . import views


urlpatterns = [    
    path('users/register/', views.register_user, name='register_user'),  # User registration endpoint
]
