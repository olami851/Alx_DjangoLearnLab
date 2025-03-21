from django.urls import path
from . import views
from .views import PostCreateView
from .views import PostListView
from .views import PostDetailView
from .views import UserLoginView
from .views import PostUpdateView
from .views import PostDeleteView

urlpatterns = [
   path('register/', views.register, name='register'),
   path('user-login/', views.user_login, name='user-login'),
   # path('login/', views.UserLoginView.as_view(), name='login')
   path('user-logout/', views.user_logout, name='user-logout'),
   path('user-profile/', views.user_profile, name='user-profile'),
   path('homepage/', views.homepage, name='homepage'),
   path('posts/new/', PostCreateView.as_view(), name='post-create'),
   path('post', PostListView.as_view(), name='post-list'),
   path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
   path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
   path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
