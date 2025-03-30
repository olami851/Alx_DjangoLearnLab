from django.urls import path
from .views import UserRegistrationView
from .views import UserLoginView
from .views import UserDetailView
from .views import FollowUserView
from .views import UnfollowUserView
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserDetailView.as_view(), name='profile'),
    path('follow/<str:username>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<str:username>/', UnfollowUserView.as_view(), name='unfollow-user'),
]
