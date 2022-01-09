from django import forms
from .models import Post, Comment


class CommentForm(forms.ModelForm):
    """docstring"""

    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author':
            forms.TextInput(attrs={'class': 'textinputclass'}),
            'text':
            forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }


class PostForm(forms.ModelForm):
    """docstring"""

    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        widgets = {
            'title':
            forms.TextInput(attrs={'class': 'textinputclass'}),
            'text':
            forms.Textarea(
                attrs={'class': 'editable medium-editor-textarea postcontent'})
        }
