from django.shortcuts import render
from UserProfile.decorators import verified_and_profile_complete_required

# Create your views here.
@verified_and_profile_complete_required()
def dashboard(request):
    return render(request, "secured/dashboard.html")