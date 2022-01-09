from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from django.utils import timezone

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post, Comment
from .forms import PostForm, CommentForm

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


###############################################################################


@login_required
def publish_post(request: HttpRequest, pk: int) -> HttpResponse:
    """docstring"""

    post: Post = get_object_or_404(Comment, pk=pk)
    post.publish()

    return redirect('post_detail', pk=pk)


@login_required
def add_comment_to_post(request: HttpRequest, pk: int) -> HttpResponse:
    """docstring"""
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.Post)

        if form.is_valid():
            comment: Comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)

    else:
        form = CommentForm()

    return render(request, 'blog/comment-form.html', {'form': form})


@login_required
def approve_comment(request: HttpRequest, pk: int) -> HttpResponse:
    """docstring"""

    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()

    return redirect('post_detail', pk=comment.post.pk)


@login_required
def remove_comment(request: HttpRequest, pk: int) -> HttpResponse:
    """docstring"""

    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()

    return redirect('post_detail', pk=post_pk)
