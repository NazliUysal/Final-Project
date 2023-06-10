from .models import ThreadModel
from django import forms

class ThreadForm(forms.Form):
    username = forms.CharField(label='', max_length=100)

    widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

class MessageForm(forms.Form):
    message = forms.CharField(label='', max_length=1000)

    widgets = {
            'message': forms.TextInput(attrs={'class': 'form-control'}),
        }