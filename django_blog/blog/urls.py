from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    search_view,
    PostByTagListView
)
from . import views

app_name = 'blog'

urlpatterns = [
     # Add the URL for posts filtered by a specific tag (using a tag slug)
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),  # New URL for posts by tag
    path('', PostListView.as_view(), name='post-list'),  # Default view for all posts
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # Detail view for a single post
    
    # Add the URL for posts filtered by a specific tag (using a tag slug)
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),  # New URL for posts by tag
]

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('search/', search_view, name='search'),
    path('tags/<str:tag>/', PostListView.as_view(), name='posts-by-tag'),

    # Authentication and Profile URLs
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),

    # Blog Post URLs
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comment URLs
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
