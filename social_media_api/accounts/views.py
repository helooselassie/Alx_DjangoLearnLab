from rest_framework import generics, status
from rest_framework import viewsets, permissions, serializers
from rest_framework.response import Response
from django.contrib.auth import authenticate
from accounts.serializers import (
    CustomUserSerializer, 
    RegisterSerializer, 
    LoginSerializer, 
    UserRegisterSerializer, 
    UserLoginSerializer, 
    UserSerializer, 
    UserDetailSerializer,
)
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import (
    CustomUserSerializer, 
    UserFollowSerializer, 
    RegisterSerializer, 
    LoginSerializer,
)    
from .models import User
from django.shortcuts import get_object_or_404, redirect
from .models import CustomUser
from rest_framework.authtoken.models import Token
from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework.permissions import AllowAny
from .serializers import RegistrationSerializer
from rest_framework.views import APIView





CustomUser.objects.all()
User = get_user_model()


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_unfollow = User.objects.get(id=user_id)
            request.user.following.remove(user_to_unfollow)  # Remove from following
            return Response({'message': f'You have unfollowed {user_to_unfollow.username}'})
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_follow = User.objects.get(id=user_id)
            request.user.following.add(user_to_follow)  # Add to following
            return Response({'message': f'You are now following {user_to_follow.username}'})
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)
class UserRegisterView(generics.CreateAPIView):    
    serializer_class = UserRegisterSerializer
    permission_classes = (permissions.AllowAny,)
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
class UserFeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Get posts from users that the current user follows
        followed_users = self.request.user.following.all()
        return Post.objects.filter(author__in=followed_users).order_by('-created_at')
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
    
class UserView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer

class UserFollowViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def follow_user(self, request, user_id):
        user_to_follow = User.objects.get(id=user_id)
        if user_to_follow != request.user:
            request.user.following.add(user_to_follow)
        return {"detail": f"{request.user.username} is now following {user_to_follow.username}"}

    def unfollow_user(self, request, user_id):
        user_to_unfollow = User.objects.get(id=user_id)
        if user_to_unfollow != request.user:
            request.user.following.remove(user_to_unfollow)
        return {"detail": f"{request.user.username} is no longer following {user_to_unfollow.username}"}         

def followuser(request, user_id):
    user_to_follow = get_object_or_404(CustomUser, id=user_id)
    request.user.customuser_set.add(user_to_follow)
    return redirect('accounts:profile', user_id=user_to_follow.id)

def unfollowuser(request, user_id):
    user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
    request.user.customuser_set.remove(user_to_unfollow)
    return redirect('accounts:profile', user_id=user_to_unfollow.id)


class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                },
                'token': token.key,
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   