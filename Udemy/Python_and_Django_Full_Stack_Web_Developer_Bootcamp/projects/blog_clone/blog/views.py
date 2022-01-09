from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)

# Create your views here.


class AboutView(TemplateView):
    """docstring"""

    template_name = 'about.html'


class PostListView(ListView):
    """docstring"""

    model = Post

    def get_queryset(self) -> None:
        """docstring"""
        return Post.objects.filter(
            published_date__lte=timezone.now).order_by('-published_date')


class PostDetailView(DetailView):
    """docstring"""

    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    """docstring"""

    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post


class PostUpdateView(LoginRequiredMixin, UpdateView):
    """docstring"""

    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    """docstring"""

    model = Post
    success_url = reverse_lazy('post_list')


class DraftListView(LoginRequiredMixin, ListView):
    """docstring"""

    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'

    model = Post

    def get_queryset(self) -> None:
        """docstring"""
        return Post.objects.filter(
            published_date__isnull=True).order_by('-published_date')
