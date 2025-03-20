from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm


# Create your views here.

def homepage(request):
    return render(request, 'blog/index.html')

def register(request):
    
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("user-login")
        
    context = {'user-registerform': form}
        
    return render(request, 'blog/register.html', context=context)
    










def user_login(request):
    return render(request, 'blog/user-login.html')

def user_logout(request):
    pass

def user_profile(request):
    pass
