from django import forms
from django.forms import widgets


class GuestBookForm(forms.Form):
    author = forms.CharField(max_length=50, required=True, label='Name')
    email = forms.EmailField(max_length=50, required=True, label='Email')
    text = forms.CharField(max_length=3000, required=True, label='text')
