from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import AddCommentView, EditCommentView, DeleteCommentView
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView

app_name = 'blog'

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('', PostListView.as_view(), name='post-list'), 
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  
    path('post/new/', PostCreateView.as_view(), name='post-create'),  
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), 
    path('post/<int:post_id>/comments/new/', AddCommentView.as_view(), name='comment-add'),
    path('comments/<int:comment_id>/edit/', EditCommentView.as_view(), name='comment-edit'),
    path('comments/<int:comment_id>/delete/', DeleteCommentView.as_view(), name='comment-delete'),    
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-edit'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('post/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment-add'),
]

urlpatterns = [
    # URL for creating a new comment on a post
    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment-create'),

    # URL for updating an existing comment
    path('comments/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),

    # URL for deleting an existing comment
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]



