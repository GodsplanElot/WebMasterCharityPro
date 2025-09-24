from django.urls import path
from . import views

app_name = "secured"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
]
