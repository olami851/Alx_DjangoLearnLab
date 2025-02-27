from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import user_passes_test



def list_books(request):
    books = Book.objects.all()
    context = {'list_books': books}
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
class SignUpView(CreateView):
    form_class = UserCreationForm()
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'    
    
# admin_view
def admin_check(user):
    return user.userprofile.role == 'Admin'

@user_passes_test(admin_check)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# librarian_view

def librarian_check(user):
    return user.userprofile.role == 'Librarian'

@user_passes_test(librarian_check)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# member_view

def member_check(user):
    return user.userprofile.role == 'Member'

@user_passes_test(member_check)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')