from django.urls import path
from django.contrib import admin
from django.urls import path, include  # Include function for app URLs
from .views import BookList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include the api app's URLs under the /api/ path
    path('books/', BookList.as_view(), name='book-list'),
]
