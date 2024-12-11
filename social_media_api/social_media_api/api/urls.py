from django.urls import path
from .views import PostListCreate, PostDetail
from .views import UserDetailAPIView
from .views import RegisterUserAPIView, LoginUserAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('posts/', PostListCreate.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('register/', RegisterUserAPIView.as_view(), name='register-user'),
    path('login/', LoginUserAPIView.as_view(), name='login-user'),
    path('user/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
