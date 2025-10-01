from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("projects/", views.projects, name="projects"),
    path("staff/", views.staff_info, name="staff_info"),
    path("policy/", views.policy, name="policy"),
]