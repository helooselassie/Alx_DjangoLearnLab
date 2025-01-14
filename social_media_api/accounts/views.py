
from accounts.serializers import (
    CustomUserSerializer, 
    RegisterSerializer, 
    LoginSerializer, 
    UserRegisterSerializer, 
    UserLoginSerializer,     
    UserDetailSerializer,
    RegistrationSerializer,
)

from .serializers import (
    CustomUserSerializer, 
    UserFollowSerializer, 
    RegisterSerializer, 
    LoginSerializer,
    RegistrationSerializer,
    UserSerializer,
)   

from rest_framework import generics, status
from rest_framework import viewsets, permissions, serializers
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model 
from .models import User
from django.shortcuts import get_object_or_404, redirect
from .models import CustomUser
from rest_framework.authtoken.models import Token
from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework.permissions import AllowAny
from .serializers import RegistrationSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import views
import logging
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView




logger = logging.getLogger(__name__)


CustomUser.objects.all()
User = get_user_model()


class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)

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

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

class UserCreateView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        print(f"Request user: {request.user}, Authenticated: {request.user.is_authenticated}")
        return super().post(request, *args, **kwargs)

class UserFeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        followed_users = self.request.user.following.all()
        return Post.objects.filter(author__in=followed_users).order_by('-created_at')


class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        print(f"Attempting login with username: {username} and password: {password}")
        
        user = authenticate(username=username, password=password)
        print(f"Authenticated user: {user}")

        if user:
            if user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                print(f"Generated token: {token.key}")
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            return Response({'error': 'User account is inactive'}, status=status.HTTP_403_FORBIDDEN)
        return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)


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

class UserDetailView(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)



class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
        
class UserListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
        return super().get(request, *args, **kwargs)

class UserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]        