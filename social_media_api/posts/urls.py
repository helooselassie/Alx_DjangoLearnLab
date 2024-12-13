from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views import FeedViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')
router = DefaultRouter()
router.register(r'feed', FeedViewSet, basename='feed')

urlpatterns = [
    path('', include(router.urls)),
]
