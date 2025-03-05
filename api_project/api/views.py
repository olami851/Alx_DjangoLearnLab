from django.shortcuts import render
from rest_framework import generics  
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
# from rest_framework.views import ListAPIView
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework.views import APIView

# Create your views here.

class BookList(generics.ListAPIView):
    querryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer