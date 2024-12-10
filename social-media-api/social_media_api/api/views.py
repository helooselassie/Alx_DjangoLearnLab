from .models import Post
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from social_media_api.urls import urlpatterns
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def user_register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            email = data.get('email')
            
            if not username or not email:
                return JsonResponse({"error": "Username and email are required."}, status=400)
            
            # Simulating user registration logic
            return JsonResponse({
                "message": "User registered successfully!",
                "username": username,
                "email": email
            }, status=201)
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
    else:
        return JsonResponse({"error": "Only POST requests are allowed"}, status=405)


@api_view(['GET'])
def fetch_all_posts(request):
    posts = Post.objects.all().values('id', 'title', 'content', 'author__username', 'created_at')
    return Response({"posts": list(posts)})

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if not username or not email or not password:
        return Response({"error": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.create_user(username=username, email=email, password=password)
        return Response({"message": "User registered successfully.", "username": user.username}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

