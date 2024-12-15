from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from django.contrib.auth.decorators import login_required
from .models import Post
from notifications.models import Notification
from .models import Like  # Ensure Like model is imported
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, generics



User = get_user_model()

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)


    if created:
        # If created, generate notification for like
        Notification.objects.create(user=post.author, message=f"{request.user.username} liked your post.")
        return Response({'message': 'Liked'}, status=status.HTTP_201_CREATED)
    else:
        # If already liked, delete the like (unlike)
        like.delete()
        return Response({'message': 'Unliked'}, status=status.HTTP_200_OK)
    

def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    # Try to get the existing Like instance
    try:
        like = Like.objects.get(user=request.user, post=post)
        like.delete()  # Delete the like if it exists
        return Response({'message': 'Unliked'}, status=status.HTTP_200_OK)
    except Like.DoesNotExist:
        return Response({'message': 'You have not liked this post'}, status=status.HTTP_400_BAD_REQUEST)


@login_required
def feed(request):
    following_users = request.user.following.all()
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    return render(request, 'posts/feed.html', {'posts': posts})

class FeedViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

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
class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()  # Adjust according to your model
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)