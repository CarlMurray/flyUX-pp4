from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='Email')
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']