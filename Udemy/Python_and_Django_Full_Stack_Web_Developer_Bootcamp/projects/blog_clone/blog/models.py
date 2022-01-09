from typing import List
from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Comment(models.Model):
    """docstring"""

    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    post = models.ForeignKey('blog.Post',
                             related_name='comments',
                             on_delete=models.CASCADE)

    def approve(self) -> None:
        """docstring"""
        self.approved_comment = True
        self.save()

    def get_absolute_url(self) -> None:
        """docstring"""
        return reverse('post_list')

    def __str__(self) -> str:
        return self.text


class Post(models.Model):
    """docstring"""

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self) -> None:
        """docstring"""
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self) -> List[Comment]:
        """docstring"""
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self) -> None:
        """docstring"""
        return reverse('post', kwargs={'pk': self.pk})

    def __str__(self) -> str:
        return self.title
