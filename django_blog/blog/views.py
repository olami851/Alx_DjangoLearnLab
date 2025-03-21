from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm
from django.views import View
from django.urls import reverse_lazy
from .models import Post
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

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


# class PostView(View):
#     def get(self, request):
#         return HttpResponse('results')

# CreateView

    
class PostListView(ListView):
    model = Post
    template_name = 'blog/listing.html'
    

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/viewing.html'
    
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/creating.html'
    fields = ['title', 'content', 'author']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
class UserLoginView(LoginView):
    template_name = 'blog/login.html'
    
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/editing.html'
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    
class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/deleting.html'
    success_url = reverse_lazy('post-list')
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author