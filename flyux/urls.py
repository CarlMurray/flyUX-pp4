"""
URL configuration for flyux project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views as core_views
from users import views as users_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", core_views.home_page, name='home-page'),
    path("login/", users_views.login_view, name="login"),
    path("logout/", users_views.logout_view, name="logout"),
    path("register/", users_views.register_view, name="register"),
    path("search_results/", core_views.search_results_view, name="search-results"),
    path("passenger_details/", core_views.passenger_details_view, name="passenger-details"),
    path("search_results/alt_dates/", core_views.alt_dates, name="alt-dates"),
    path("checkout/", core_views.checkout_view, name="checkout"),
    path("order_confirmation/", core_views.order_confirmation_view, name="order-confirmation"),
    path("bookings/", core_views.bookings_view, name="bookings"),
    path("bookings/detail/<int:booking_id>", core_views.bookings_detail_view, name="bookings-detail"),
    path("bookings/detail/edit/<int:booking_id>", core_views.bookings_edit_view, name="bookings-edit"),
]
