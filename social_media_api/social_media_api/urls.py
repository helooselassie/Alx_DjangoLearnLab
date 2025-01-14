"""
URL configuration for social_media_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from accounts.views import LoginView
from rest_framework.authtoken import views
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.urls import path, include
from accounts.views import UserListView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', UserListView.as_view(), name='user-list'),
    path('api/users/login/', LoginView.as_view(), name='login'),
    path('api/users/', include('accounts.urls')),
    path('api/posts/', include('posts.urls')),
    path('api/notifications/', include('notifications.urls')),
    path('api/', include('accounts.urls')),
    path('api/', include('posts.urls')),    
    path('accounts/', include('accounts.urls')),  
    path('posts/', include('posts.urls')), 
    path('', include('posts.urls')),   
    path('', include('accounts.urls')),    
    path('api-token-auth/', views.obtain_auth_token, name='api_token_auth'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('api/login/', LoginView.as_view(), name='login'),
    #path('', include('social_media_api.urls')),
]
