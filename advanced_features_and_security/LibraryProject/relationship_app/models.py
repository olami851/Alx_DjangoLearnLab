from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# from advanced_features_and_security.LibraryProject.LibraryProject.settings import AUTH_USER_MODEL

# from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    
    class Meta:
        permissions= [
            ('can_add_book', 'can add book'),
            ('can_change_book', 'can change book'),
            ('can_delete_book', 'can delete book')
        ]
    def __str__(self):
        return self.title
    
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name="books")
    
    def __str__(self):
        return self.name
    
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE,)
    
    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    Role_choices = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=Role_choices)
    
    def __str__(self):
        return f"{self.user.username}'s profile"
    
class Profile(models.Model):
    user = models.OneToOneField(settings, AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField()