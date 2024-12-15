from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views import FeedViewSet
from rest_framework.routers import DefaultRouter
from .views import like_post, unlike_post
from . import views
from .views import PostListView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')
router = DefaultRouter()
router.register(r'feed', FeedViewSet, basename='feed')

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', views.feed, name='feed'),
    path('api/posts/', PostListView.as_view(), name='post-list'),
    path('<int:pk>/like/', views.like_post, name='like_post'),
    path('<int:pk>/unlike/', unlike_post, name='unlike-post'),
    
]
