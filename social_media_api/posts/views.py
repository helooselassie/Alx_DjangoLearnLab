from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.IsAuthenticatedOrWriteOnly]

    def get_queryset(self):
        return Comment.objects.filter(post__in=self.request.user.is_authenticated and self.request.user.posts.all() or Post.objects.all())

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.IsAuthenticatedOrWriteOnly]

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user if self.request.user.is_authenticated else None)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)