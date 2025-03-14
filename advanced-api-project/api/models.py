from django.db import models

# Create your models here.

class Author(models.Model):
    
    """
        Author model: Represent a model of an author with single or multiple books.
        Field:
            name: This represent the full name of the author 
    """
    name = models.CharField(max_length=200)
    
    def __st__(self):
        return self.name

class Book(models.Model):
    
    """
        Book model: Describe a book written by an author with the following fields:
            Fields:
                title: the title of the book 
                publication_year: the year in which the book was published and 
                made available to the general public
                author: foreign key relationship in which an author can have 
                multiple books to his/her publication.  
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="book", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title, self.author