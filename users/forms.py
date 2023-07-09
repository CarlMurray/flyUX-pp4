from django import forms
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='Email')
    password = forms.CharField(widget=forms.PasswordInput)
