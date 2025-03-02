from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django

# Create your views here.

def index(request):
    return HttpResponse("Welcome to my bookshelf app.")

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    all_books = [
        {'id': 1, 'title': 'python', 'author': 'olami'},
        {'id':2, 'title': 'django', 'author': 'femi'},
    ]
    return render(request, 'bookshelf/view.html', {'all_books': all_books})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            
            
