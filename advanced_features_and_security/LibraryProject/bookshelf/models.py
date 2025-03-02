from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    class Meta:
        permissions = [
            ('can_view', 'Can View'),
            ('can_create', 'Can Create'),
            ('can_edit', 'Can Edit'),
            ('can_delete', 'Can Delete'),
        ]
    
    def __str__(self):
        return self.title
    
   
class CustomUserManager(BaseUserManager):
    def create_user(self, username = None, email = None, date_of_birth = None, password=None, profile_photo = None):
        pass
        
     
    def create_superuser(self):
        pass
      
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True)
    profile_photo = models.ImageField(upload_to='profile_photo/', null=True, blank=True)
    
    def __str__(self):
        return self.username
    
class UserProfile(models.Model):
        
    Role_choices = [
            ('Admin', 'Admin'),
            ('Librarian', 'Librarian'),
            ('Member', 'Member'),
        ]
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='bookshelf_userprofile')
    role = models.CharField(max_length=50, choices=Role_choices)
    
    def __str__(self):
        return self.username
    
