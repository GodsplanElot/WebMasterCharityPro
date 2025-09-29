from django.urls import path
from . import views

app_name = "profile"   # <-- add this

urlpatterns = [
    path("wizard/start/", views.wizard_start, name="wizard_start"),
]
