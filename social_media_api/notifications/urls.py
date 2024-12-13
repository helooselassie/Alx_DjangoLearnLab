from django.urls import path
from . import views

urlpatterns = [
    path('', views.NotificationList.as_view(), name='notifications'),
]