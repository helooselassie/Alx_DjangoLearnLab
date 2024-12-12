from django.urls import path
from .views import UserRegisterView, UserLoginView, UserDetailAPIView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('user/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
]
