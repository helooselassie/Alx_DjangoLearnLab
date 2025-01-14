from django.urls import path, include
from .views import RegisterView, LoginView
from .views import UserFollowViewSet
from rest_framework.routers import DefaultRouter
from . import views
from .views import RegisterView
from .views import LoginView
from .views import RegistrationView
from .views import UserDetailView
from .views import UserListView
from .views import UserCreateView

router = DefaultRouter()
router.register(r'follow', UserFollowViewSet, basename='follow')

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),  # List all users
    path('', UserCreateView.as_view(), name='user-create'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),  # Get user by ID
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('', include(router.urls)),
    path('api/user/register/', RegisterView.as_view(), name='user-register'),
    path('api/register/', RegistrationView.as_view(), name='register'),
    path('api/users/login/', LoginView.as_view(), name='login'),
    path('follow/<int:user_id>/', views.followuser, name='followuser'),
    path('unfollow/<int:user_id>/', views.unfollowuser, name='unfollowuser'),
    path('api/users/register/', RegisterView.as_view(), name='register'),
    path('users/register/', RegisterView.as_view(), name='register'),
]