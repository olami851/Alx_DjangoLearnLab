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
   path('post/new/', PostCreateView.as_view(), name='post-create'),
   path('post', PostListView.as_view(), name='post-list'),
   path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
   path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
   path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
