from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import logout, login, authenticate
from flyux import urls
from .forms import LoginForm, RegistrationForm
from django.forms import Form


def logout_view(request):
    logout(request)
    return redirect('home-page')
    
    
def signup_view(request):
    pass


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        data = {
            'username':email,
            'password':password
        }
        form = LoginForm(data=data)
        if form.is_valid():
            form = form.cleaned_data
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home-page')
            else:
                print('ERROR MSG TO BE ADDED')
        else:
            print('TBD')
    return render(request, 'users/login.html')


def register_view(request):
    # RETURN HOME IF USER TRIES TO REGISTER WHILE SIGNED IN
    if request.user.is_authenticated:
            return redirect('home-page')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home-page')
    form = RegistrationForm()    
    return render(request, 'users/register.html', {'form':form})
