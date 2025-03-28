from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content', 'published_date')
    search_fields = ('title', 'author')
    
admin.site.register(Post, PostAdmin)
