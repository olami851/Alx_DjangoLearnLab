from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    """
        BookSerializer: Handles all books and also include the validation
        of the publication year  
    """
    class Meta:
        model = Book
        field = '__all__'
        
    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year
            raise serializers.ValidationError(f"Publication year {value} can not be in the future....")
        return value
        
class AuthorSerializer(serializers.ModelSerializer):
    """
        AuthorSerializer: this includes the name field and also a nested BookSerializer. 
    """
    books = BookSerializer(many=True, read_only= True)
    
    class Meta:
        model = Author
        field = ['name', 'books']