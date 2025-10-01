from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "pages/home.html")

def about(request):
    return render(request, "pages/about.html")

def projects(request):
    return render(request, "pages/projects.html")

def policy(request):
    return render(request, "pages/policy.html")

def contact(request):
    # Dummy contact page - no real processing (you asked simple)
    return render(request, "pages/contact.html")

def staff_info(request):
    return render(request, "pages/staff_info.html")