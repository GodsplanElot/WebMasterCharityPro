from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import views as auth_views

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:signup_success")
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/signup.html", {"form": form})

def signup_success(request):
    return render(request, "accounts/signup_success.html")
