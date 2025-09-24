from django.urls import path
from . import views

app_name = "UserPorile"

urlpatterns = [
    path("wizard/start/", views.wizard_start, name="wizard_start"),
]
