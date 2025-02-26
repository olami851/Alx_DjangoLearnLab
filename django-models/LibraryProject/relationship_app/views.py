from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Library
from django.views.generic import DetailView


def list_books(request):
    books = Book.objects.all()
    context = {'list_books': books}
    return render(request, 'books/list_books.html', context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library/library_detail.html'
    context_object_name = 'library'
    