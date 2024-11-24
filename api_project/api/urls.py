from django.contrib import admin
from django.urls import path, include  # Include function for app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include the api app's URLs under the /api/ path
]
