from django.shortcuts import render
from rest_framework.generics import ListAPIView # type: ignore
from .models import Book
from .serializers import BookSerializer

# Create your views here.

class BookList(ListAPIView):
    querryset = Book.objects.all()
    serializer_class = BookSerializer
