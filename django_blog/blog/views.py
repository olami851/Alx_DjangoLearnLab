from django.shortcuts import render, redirect, get_object_or_404
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
from django.contrib.auth.decorators import login_required
from .models import Comment
from .forms import CommentForm

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
    template_name = 'blog/post_list.html'
    
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_create.html'
    fields = ['title', 'content', 'author']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
class UserLoginView(LoginView):
    template_name = 'blog/login.html'
    
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    
class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post-list')
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context("comments") = self.object.comments.all()
        context("form") = CommentForm()
        return context
    
    
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_create.html'
    
    
    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the comment author
        form.instance.post = get_object_or_404(Post, id=self.kwargs["post_id"])  # Link to post
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"pk": self.kwargs["post_id"]})
    
    
class CommentUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
        
     model = Post
     template_name = 'blog/comment_edit.html'
     form_class = CommentForm
        
     def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
     def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"pk": self.object.post.id})
        
        
     def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
        
        
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "blog/comment_delete.html"

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"pk": self.object.post.id})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author  # Only author can delete
        