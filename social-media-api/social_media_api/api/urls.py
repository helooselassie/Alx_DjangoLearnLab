from django.urls import path
from . import views
from .views import user_register



urlpatterns = [    
    path('users/register/', user_register, name='user-register'),
    path('users/register/', views.register_user, name='register_user'),  # User registration endpoint
]
