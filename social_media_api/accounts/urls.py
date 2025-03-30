from django.urls import path
from .views import UserRegistrationView
from .views import UserLoginView
from .views import UserDetailView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserDetailView.as_view(), name='profile')
]
