from django.urls import path
from . import views
from .views import NotificationListView

urlpatterns = [
    path('', views.NotificationList.as_view(), name='notifications'),
    path('', NotificationListView.as_view(), name='notification_list'),
]