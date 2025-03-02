from django.contrib import admin
from .models import Book
from .models import CustomUser
from .models import CustomUserManager
from django.conf import settings
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_filter = ("title", "author", "publication_year")
    search_fields = ("title", "author")
    
admin.site.register(Book, BookAdmin)


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_of_birth', 'profile_photo')  
admin.site.register(CustomUser, CustomUserAdmin)