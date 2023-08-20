from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import logout, login, authenticate
from flyux import urls
from .forms import LoginForm, RegistrationForm
from django.forms import Form
from django.contrib import messages


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home-page')


def login_view(request):
    # STORE PREV URL FOR REDIRECT AFTER LOGIN, TRIMS '?next='
    request.session['next_url'] = request.GET.urlencode(safe='/?=&')[5:]
    if request.user.is_authenticated:
        return redirect('home-page')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        data = {
            'username': email,
            'password': password
        }
        form = LoginForm(data=data)
        if form.is_valid():
            form = form.cleaned_data
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(request.session['next_url'])
            else:
                messages.error(request, 'Invalid email or password.')
    return render(request, 'users/login.html')


def register_view(request):
    request.session['next_url'] = request.GET.urlencode(safe='/?=&')[5:]
    # RETURN HOME IF USER TRIES TO REGISTER WHILE SIGNED IN
    if request.user.is_authenticated:
        return redirect('home-page')
    # IF CLICKING SIGNUP LINK
    if request.method == 'GET':
        form = RegistrationForm()
        return render(request, 'users/register.html', {'form': form})
    # IF SIGNING UP FROM PASSENGER DETAILS PAGE
    if request.POST.get('next'):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/passenger_details/?' + request.POST.get('next'))
    # IF SUBMITTING REGISTER FORM FROM REGISTER PAGE
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(request.session['next_url'])