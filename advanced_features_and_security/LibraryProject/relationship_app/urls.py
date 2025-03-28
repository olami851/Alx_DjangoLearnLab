from django.urls import path
from . import views
from .views import list_books
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import admin_view
from .views import librarian_view
from .views import member_view
from .views import add_book
from .views import edit_book
from .views import delete_book


urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html', name='login')),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register(template_name='relationship_app/register.html'), name='register'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view')
    path('books/add/', add_book, name='add_book/'),
    path('books/<int:pk/edit/>', edit_book, name='edit_book/'),
    path('books/<int:pk/delete/', delete_book, name='delete_book/'),
]