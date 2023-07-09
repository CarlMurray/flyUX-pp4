from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import logout, login, authenticate
from flyux import urls
from .forms import LoginForm
from django.forms import Form


def logout_view(request):
    logout(request)
    return redirect('home-page')
    
    
def signup_view(request):
    pass


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        password = request.POST.get('password')
        print(password)
        data = {
            'username':email,
            'password':password
        }
        form = LoginForm(data=data)
        if form.is_valid():
            form = form.cleaned_data
            print(form)
            user = authenticate(request, email=email, password=password)
            if user is not None:
                print('yepp')
                login(request, user)
                return redirect('home-page')
            else:
                print('ERROR MSG TO BE ADDED')
        else:
            print('TBD')
    return render(request, 'users/login.html')