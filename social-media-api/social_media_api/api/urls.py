from django.urls import path
from .views import PostListCreate, PostDetail

urlpatterns = [
    path('posts/', PostListCreate.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
]
