from django.urls import path
from . import views
from .views import list_books
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html', name='login')),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register(template_name='relationship_app/register.html'), name='register'),
]