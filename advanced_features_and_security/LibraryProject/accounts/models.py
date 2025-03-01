from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None, **kwargs):
        
        if not email:
            raise ValueError('Email field is required...')
        
        email = self.normalize_email(email)
        user = self.model(email=email, data_of_birth=date_of_birth, **kwargs )
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_supertuser(self, email, date_of_birth, password=None, **kwarg):
        user = self.create_user(email, date_of_birth, password)
        
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True)
    profile_photo = models.ImageField(upload_to='profile_photo/', null=True, blank=True)
    
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['date_of_birth', 'profile_photo']
    
    objects = CustomUserManager()
