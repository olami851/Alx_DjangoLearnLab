from django.urls import path
from . import views
from .views import PostCreateView
from .views import PostListView
from .views import PostDetailView
from .views import UserLoginView
from .views import PostUpdateView
from .views import PostDeleteView
from .views import CommentCreateView
from .views import CommentUpdateView
from .views import CommentDeleteView


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
   path('post/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
   path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comments-update'),
   path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comments-delete')
]
