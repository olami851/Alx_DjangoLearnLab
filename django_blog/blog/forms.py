from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post
from .models import Comment

class CreateUserForm(UserCreationForm):
    
    class Meta:
        model = User
        field = ['username', 'email', 'password1', 'password2']
        exclude = ['last_login']
        
        
class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']
        
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['content']
        
        def clean_content(self):
            content = self.clean_data.get('content')
            
            if content < 5:
                raise forms.ValidationError("Comment must be at least 5 character long")
            
            if content > 500:
                raise forms.ValidationError("Comment can only be between 5 to 500 character long")
            
            if "badword" in content.lower():
                raise forms.ValidationError("Comment contains inappropriate words.")
            
            return content