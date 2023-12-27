# my_app/views.py

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Post, Comment

class NewsListView(ListView):
    model = Post
    template_name = 'news_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

class CreatePostView(PermissionRequiredMixin, CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = ['title', 'content']
    permission_required = 'my_app.add_post'  # Замените на ваше

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
