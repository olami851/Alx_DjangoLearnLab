from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment
from .serializers import CommentSerializer, PostSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import StandardResultSetPagination

# Create your views here.

class IsAuthorOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = IsAuthorOrReadOnly
    pagination_class = StandardResultSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title', 'content']
    search_fields = ['title', 'content']
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = IsAuthorOrReadOnly
    pagination_class = StandardResultSetPagination
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')