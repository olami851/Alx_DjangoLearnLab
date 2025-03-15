from django.urls import path
from .views import BookListView
from .views import BookCreateView
from .views import BookDetailView
from .views import BookUpdateView
from .views import BookDeleteView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk/>', BookDetailView.as_view(), name='book-detail'),
    path('books/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk/>', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk/>', BookDeleteView.as_view(), name='book-delete'),
    
]
