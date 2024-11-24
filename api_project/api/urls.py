from django.urls import path
from django.contrib import admin
from django.urls import path, include  # Include function for app URLs
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include the api app's URLs under the /api/ path
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
]
