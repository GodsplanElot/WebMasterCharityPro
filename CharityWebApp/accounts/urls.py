# accounts/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.shortcuts import render

app_name = "accounts"

urlpatterns = [
    path("signup/", views.signup, name="signup"),

    # login (we use the default LoginView but you must create a login template)
    # New
    path("login/", views.CustomLoginView.as_view(), name="login"),


    path('signup-success/', lambda r: render(r, 'accounts/signup_success.html'), name='signup_success'),

     path("not-verified/", views.not_verified, name="not_verified"),

    # logout
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
