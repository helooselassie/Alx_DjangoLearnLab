from rest_framework import viewsets, permissions, response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .models import Post, models
from .serializers import PostSerializer


User = get_user_model()



class FeedViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        user_posts = User.objects.filter(
            following__in=request.user.followers.all()
        ).annotate(
            total_posts=models.Count('post')
        ).order_by('-total_posts__count')
        posts = Post.objects.filter(author__in=user_posts)

        serializer = PostSerializer(posts, many=True)

        return response(serializer.data)
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(post__author=self.request.user if self.request.user.is_authenticated else None)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user if self.request.user.is_authenticated else None)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)