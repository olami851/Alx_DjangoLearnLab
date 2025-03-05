from django.shortcuts import render
from rest_framework.generics import ListAPIView 
from .models import Book
from .serializers import BookSerializer
from rest_framework.views import ListAPIView
from rest_framework.response import Response


# Create your views here.

class BookList(ListAPIView):
    querryset = Book.objects.all()
    serializer_class = BookSerializer
