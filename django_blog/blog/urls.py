from django.urls import path
from . import views

urlpatterns = [
   path('register/', views.register, name='register'),
   path('user-login/', views.user_login, name='user-login'),
   path('user-logout/', views.user_logout, name='user-logout'),
   path('user-profile/', views.user_profile, name='user-profile'),
   path('homepage/', views.homepage, name='homepage')
]
