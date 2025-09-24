from django.contrib import admin
from .models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "verified", "completed", "phone")
    list_filter = ("verified", "completed", "marital_status")
    search_fields = ("user__username", "user__email", "phone")