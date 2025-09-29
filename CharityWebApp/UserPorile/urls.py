from django.urls import path
from . import views

app_name = "profile"

urlpatterns = [
    path("wizard/start/", views.wizard_start, name="wizard_start"),
    path("wizard/personal/", views.personal, name="personal"),
    path("wizard/address/", views.address, name="address"),
    path("wizard/professional/", views.professional, name="professional"),
    path("wizard/payment/bank/", views.payment_bank, name="payment_bank"),
    path("wizard/payment/card/", views.payment_card, name="payment_card"),
    path("wizard/media/", views.media, name="media"),
    path("wizard/review/", views.review, name="review"),
]
