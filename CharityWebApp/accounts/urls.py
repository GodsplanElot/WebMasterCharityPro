# accounts/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.signup, name="signup"),

    # login (we use the default LoginView but you must create a login template)
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),

    # logout
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
