# userprofile/admin.py
from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "id", "user", "first_name", "middle_name", "other_names",
        "phone_number", "is_verified", "date_created", "last_updated"
    )
    list_filter = ("is_verified", "gender", "marital_status", "date_created")
    search_fields = ("first_name", "middle_name", "other_names", "phone_number", "user__email")
