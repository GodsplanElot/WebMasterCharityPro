from django import forms
from .models import Profile

# Add bootstrap form-control classes via widgets for nice layout
class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["first_name", "middle_name", "other_names", "date_of_birth", "gender", "marital_status", "phone_number", "alternate_email"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "First name"}),
            "middle_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Middle name (optional)"}),
            "other_names": forms.TextInput(attrs={"class": "form-control", "placeholder": "Other names"}),
            "date_of_birth": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "gender": forms.Select(attrs={"class": "form-select"}),
            "marital_status": forms.Select(attrs={"class": "form-select"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
            "alternate_email": forms.EmailInput(attrs={"class": "form-control"}),
        }

class AddressForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["address_line1", "address_line2", "city", "state", "country", "postal_code"]
        widgets = {
            "address_line1": forms.TextInput(attrs={"class": "form-control"}),
            "address_line2": forms.TextInput(attrs={"class": "form-control"}),
            "city": forms.TextInput(attrs={"class": "form-control"}),
            "state": forms.TextInput(attrs={"class": "form-control"}),
            "country": forms.TextInput(attrs={"class": "form-control"}),
            "postal_code": forms.TextInput(attrs={"class": "form-control"}),
        }

class ProfessionalForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["occupation", "organization", "bio", "languages_spoken", "skills"]
        widgets = {
            "occupation": forms.TextInput(attrs={"class": "form-control"}),
            "organization": forms.TextInput(attrs={"class": "form-control"}),
            "bio": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "languages_spoken": forms.TextInput(attrs={"class": "form-control", "placeholder": "English, Yoruba"}),
            "skills": forms.TextInput(attrs={"class": "form-control", "placeholder": "First Aid, Logistics"}),
        }

class PaymentBankForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bank_name", "account_number", "account_name", "routing_number", "iban", "ssn"]
        widgets = {
            "bank_name": forms.TextInput(attrs={"class": "form-control"}),
            "account_number": forms.TextInput(attrs={"class": "form-control"}),
            "account_name": forms.TextInput(attrs={"class": "form-control"}),
            "routing_number": forms.TextInput(attrs={"class": "form-control"}),
            "iban": forms.TextInput(attrs={"class": "form-control"}),
            "ssn": forms.TextInput(attrs={"class": "form-control", "placeholder": "XXX-XX-XXXX"}),
        }

class PaymentCardForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["card_holder_name", "card_number", "expiry_date", "cvv"]
        widgets = {
            "card_holder_name": forms.TextInput(attrs={"class": "form-control"}),
            "card_number": forms.TextInput(attrs={"class": "form-control", "placeholder": "1234 5678 9012 3456"}),
            "expiry_date": forms.TextInput(attrs={"class": "form-control", "placeholder": "MM/YY"}),
            "cvv": forms.TextInput(attrs={"class": "form-control", "placeholder": "CVV"}),
        }

class MediaForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["profile_picture", "gallery_image", "intro_video"]
