from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post

class CreateUserForm(UserCreationForm):
    
    class Meta:
        model = User
        field = ['username', 'email', 'password1', 'password2']
        exclude = ['last_login']
        
        
class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'author'] 