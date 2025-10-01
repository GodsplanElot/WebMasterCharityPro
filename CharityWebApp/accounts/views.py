# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse
from .forms import CustomUserCreationForm


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. You can log in now.")
            return redirect("accounts:login")
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/signup.html", {"form": form})


def not_verified(request):
    return render(request, "accounts/not_verified.html")


class CustomLoginView(LoginView):
    template_name = "accounts/login.html"

    def get_success_url(self):
        """
        Decide where to redirect the user after login:
        - If profile not complete → wizard_start
        - If complete but not verified → accounts:not_verified
        - If verified → secured:dashboard
        """
        user = self.request.user
        profile = getattr(user, "profile", None)

        if not profile:
            return reverse("UserPorile:wizard_start")

        if not profile.completed:
            return reverse("UserPorile:wizard_start")

        if not profile.is_verified:   # ✅ use the correct field name
            return reverse("accounts:not_verified")

        return reverse("secured:dashboard")
