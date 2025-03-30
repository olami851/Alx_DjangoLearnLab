from django.urls import path
# from .views import NotificationListView, MarkNotificationAsReadView
from . import views

urlpatterns = [
    path('notifications/', NotificationListView.as_view(), name='notification-list'),
    path('notifications/<int:notification_id>/read/', MarkNotificationAsReadView.as_view(), name='mark-notification-read'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_notifications, name='view_notifications'),
    # Add other URL patterns here
]
