from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "pages/home.html")

def about(request):
    return render(request, "pages/about.html")

def contact(request):
    # Dummy contact page - no real processing (you asked simple)
    return render(request, "pages/contact.html")
