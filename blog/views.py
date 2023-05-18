from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from django.urls.base import reverse_lazy
from .models import Post
from .forms import PostForm, EditForm

# Create your views here.
'''HOME VIEW'''
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'
    
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    '''fields = '__all__' '''
    
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    '''fields = ['title', 'title_tag', 'body']'''
    
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')