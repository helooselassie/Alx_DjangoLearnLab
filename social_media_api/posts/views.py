from rest_framework import viewsets, permissions, response
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render
from .models import Post, models
from .serializers import PostSerializer
from django.contrib.auth.decorators import login_required
from .models import Post
from .views import like_post, Like
from django.shortcuts import render
from .signals import generate_notification_on_like
from notifications.models import Notification
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes



User = get_user_model()

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if not created:
        like.delete()

        # Generate notification for unlike
        generate_notification_on_like(sender=Like, instance=like, created=False)

        return Response({'message': 'Unliked'}, status=status.HTTP_200_OK)

    # Generate notification for like
    generate_notification_on_like(sender=Like, instance=like, created=True)

    return Response({'message': 'Liked'}, status=status.HTTP_200_OK)



def like_post(request):
    post = get_object_or_404, in get_object_or_404
    post = get_object_or_404(
        pk=request.GET.get('pk')
    )




@login_required
def feed(request):
    following_users = request.user.following.all()
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    return render(request, 'posts/feed.html', {'posts': posts})

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