from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import logout, login, authenticate
from flyux import urls
from .forms import LoginForm, RegistrationForm
from django.forms import Form
from django.contrib import messages


def logout_view(request):
    """
    Summary:
        Logs out the user and redirects to home page.
        
    Returns:
        redirect: Redirects to home page.
    """
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("home-page")


def login_view(request):
    """
    Summary:
        Logs in the user and redirects to home page or previous page.
    
    Returns:
        GET: Renders login page.
        POST: Logs in user and redirects to home page or previous page.
        Already logged in: Redirects to home page.
    """
    # STORE PREV URL FOR REDIRECT AFTER LOGIN, TRIMS '?next='
    request.session["next_url"] = request.GET.urlencode(safe="/?=&")[5:]
    # CHECK IF USER IS ALREADY LOGGED IN AND REDIRECT TO HOME PAGE
    if request.user.is_authenticated:
        return redirect("home-page")
    # IF SENDING LOGIN FORM
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        data = {"username": email, "password": password}
        # CHECK IF FORM IS VALID
        form = LoginForm(data=data)
        if form.is_valid():
            form = form.cleaned_data
            user = authenticate(request, email=email, password=password)
            # IF USER EXISTS, LOG IN AND REDIRECT TO PREV URL
            if user is not None:
                login(request, user)
                return redirect(request.session["next_url"])
            # ELSE, RETURN ERROR MESSAGE AND RENDER LOGIN PAGE
            else:
                messages.error(request, "Invalid email or password.")
    return render(request, "users/login.html")


def register_view(request):
    """
    Summary:
        Registers the user and redirects to home page or previous page.
        
    Returns:
        GET: Renders register page.
        POST: Registers user and redirects to home page or previous page.
        Next URL: Redirects to next URL.
        Already logged in: Redirects to home page.
    """
    request.session["next_url"] = request.GET.urlencode(safe="/?=&")[5:]
    # RETURN HOME IF USER TRIES TO REGISTER WHILE SIGNED IN
    if request.user.is_authenticated:
        return redirect("home-page")
    # IF CLICKING SIGNUP LINK
    if request.method == "GET":
        form = RegistrationForm()
        return render(request, "users/register.html", {"form": form})
    # IF SIGNING UP FROM PASSENGER DETAILS PAGE
    if request.POST.get("next"):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/passenger_details/?" + request.POST.get("next"))
    # IF SUBMITTING REGISTER FORM FROM REGISTER PAGE
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(request.session["next_url"])
