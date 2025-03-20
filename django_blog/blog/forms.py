from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    
    class Meta:
        model = User
        field = ['username', 'email', 'password1', 'password2']
        exclude = ['last_login']