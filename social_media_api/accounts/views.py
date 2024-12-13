from rest_framework import generics, status
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.contrib.auth import authenticate
from accounts.serializers import CustomUserSerializer, RegisterSerializer, LoginSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer, UserFollowSerializer, RegisterSerializer, LoginSerializer
from .models import User, follow
from django.shortcuts import get_object_or_404
from .models import CustomUser



User = get_user_model()
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    
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