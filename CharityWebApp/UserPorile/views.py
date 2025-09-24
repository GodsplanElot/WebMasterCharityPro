from django.shortcuts import render

# Create your views here.

def wizard_start(request):
    # Simple placeholder until we build the wizard
    return render(request, "UserPorile/wizard_start.html")