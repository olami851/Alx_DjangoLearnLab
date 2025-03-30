from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment, Like
from .serializers import CommentSerializer, PostSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import StandardResultSetPagination
from notifications.models import Notification
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

User = get_user_model()

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
    
    

    
class LikePostView(APIView):
    
    permission_classes = [permissions.IsAuthenticated]
    

    def post(self, request, *args, **kwargs):
        post = Post.objects.get(id=kwargs['post_id'])
        user = request.user
        if Like.objects.filter(post=post, user=user).exists():
            return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)
        Like.objects.create(post=post, user=user)
        Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb='liked',
            target=post
        )
        return Response({"detail": "Post liked."}, status=status.HTTP_200_OK)

class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        post = Post.objects.get(id=kwargs['post_id'])
        user = request.user
        like = Like.objects.filter(post=post, user=user).first()
        if not like:
            return Response({"detail": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)
        like.delete()
        Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb='unliked',
            target=post
        )
        return Response({"detail": "Post unliked."}, status=status.HTTP_200_OK)