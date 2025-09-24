from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

MARITAL_STATUS_CHOICES = [
    ("single", "Single"),
    ("married", "Married"),
    ("divorced", "Divorced"),
    ("widowed", "Widowed"),
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address1 = models.CharField("Address line 1", max_length=255, blank=True, null=True)
    address2 = models.CharField("Address line 2", max_length=255, blank=True, null=True)
    city = models.CharField(max_length=120, blank=True, null=True)
    country = models.CharField(max_length=120, blank=True, null=True)
    marital_status = models.CharField(max_length=20, choices=MARITAL_STATUS_CHOICES, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    dob = models.DateField("Date of birth", blank=True, null=True)
    verified = models.BooleanField(default=False)   # admin toggles this in admin
    completed = models.BooleanField(default=False)  # mark wizard completed

    def __str__(self):
        return f"Profile for {self.user.username}"
