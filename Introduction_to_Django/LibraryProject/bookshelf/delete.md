from bookshelf.models import Book

book.delete()
book = Book.objects.all()
print(book)