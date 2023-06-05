from django.forms import ModelForm
from .models import Post, Comment
from django import forms

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['art_name', 'image', 'caption']

        widgets = {
            'art_name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'caption': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']