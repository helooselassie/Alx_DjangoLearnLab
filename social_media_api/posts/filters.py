import django_filters
from .models import Post
from rest_framework import viewsets

class PostFilter(django_filters.rest_framework.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    content = django_filters.CharFilter(field_name='content', lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ['title', 'content']

from .filters import PostFilter

# ...

class PostViewSet(viewsets.ModelViewSet):
    # ...
    filterset_class = PostFilter