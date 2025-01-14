from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views import FeedViewSet
from rest_framework.routers import DefaultRouter
from .views import like_post, unlike_post
from . import views
from .views import PostListView, PostListCreateView, PostDetailView
from .views import PostCreateView
from .views import PostView
from .views import PostListCreateView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')
router = DefaultRouter()
router.register(r'feed', FeedViewSet, basename='feed')

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', views.feed, name='feed'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('posts/', PostView.as_view(), name='posts'),
    path('posts/', PostCreateView.as_view(), name='post-create'),
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('api/posts/', PostCreateView.as_view(), name='post-create'),
    path('api/posts/', PostListView.as_view(), name='post-list'),
    path('<int:pk>/like/', views.like_post, name='like_post'),
    path('<int:pk>/unlike/', unlike_post, name='unlike-post'),
    path('', PostListCreateView.as_view(), name='post-list-create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'), 
    path('', PostListView.as_view(), name='post-list'),     
    path('', PostView.as_view(), name='post-view'), 
    path('users/posts/', PostCreateView.as_view(), name='user-post-create'),  # Adjust the view
]
