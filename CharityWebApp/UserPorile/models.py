from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")

    # Personal Info
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    other_names = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)

    MARITAL_CHOICES = [
        ("Single", "Single"),
        ("Married", "Married"),
        ("Divorced", "Divorced"),
        ("Widowed", "Widowed"),
    ]
    marital_status = models.CharField(max_length=10, choices=MARITAL_CHOICES, blank=True, null=True)

    # Contact Info
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    alternate_phone_number = models.CharField(max_length=20, blank=True, null=True)
    alternate_email = models.EmailField(blank=True, null=True)

    # Addresses
    address_line1 = models.CharField(max_length=255, blank=True, null=True)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)

    # Professional/Other
    occupation = models.CharField(max_length=100, blank=True, null=True)
    organization = models.CharField(max_length=150, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    languages_spoken = models.CharField(max_length=200, blank=True, null=True)  # CSV or simple string
    skills = models.CharField(max_length=300, blank=True, null=True)  # CSV

    # Verification
    ssn = models.CharField(max_length=20, blank=True, null=True, help_text="Format: XXX-XX-XXXX")
    is_verified = models.BooleanField(default=False)

    # Payment details
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    account_number = models.CharField(max_length=30, blank=True, null=True)
    account_name = models.CharField(max_length=150, blank=True, null=True)
    routing_number = models.CharField(max_length=30, blank=True, null=True)
    iban = models.CharField(max_length=34, blank=True, null=True)

    card_holder_name = models.CharField(max_length=150, blank=True, null=True)
    card_number = models.CharField(max_length=16, blank=True, null=True)
    expiry_date = models.CharField(max_length=5, blank=True, null=True)  # MM/YY
    cvv = models.CharField(max_length=4, blank=True, null=True)

    # Media
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    gallery_image = models.ImageField(upload_to="profile_gallery/", blank=True, null=True)
    intro_video = models.FileField(upload_to="profile_videos/", blank=True, null=True)

    # Admin/flow fields
    setup_completed = models.BooleanField(default=False)  # marks wizard completion
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        names = " ".join(filter(None, [self.first_name, self.middle_name, self.other_names]))
        return f"{names or self.user.get_full_name() or self.user.email}"
