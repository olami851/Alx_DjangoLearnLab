from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import permissions
from datetime import date
from rest_framework import filters
from django_filters import rest_framework
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'author', 'publication_year']
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author']
    filter_backends = [filters.OrderingFilter]
    order_fields = ['title', 'publication_year']

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        if Book.objects.filter(title=title).exists():
            raise serializer.ValidationError(f"{title}: A book with the titke already exist")
        
        serializer.save(added_by=self.request.user)

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_update(self, serializer):
        book = self.get_object()
        if book.added_by != self.request.user:
            raise serializer.ValidationError({"error": "You can only update a book that you created"})
        
        serializer.save(updated_by=self.request.user)
        

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]