from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from .forms import (PersonalInfoForm, AddressForm, ProfessionalForm,
                    PaymentBankForm, PaymentCardForm, MediaForm)


@login_required
def wizard_start(request):
    # entry page; send to personal step if not completed
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if profile.setup_completed:
        return redirect("secured:dashboard")
    return redirect("profile:personal")


@login_required
def personal(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = PersonalInfoForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Personal info saved.")
            return redirect("profile:address")
    else:
        form = PersonalInfoForm(instance=profile)
    return render(request, "UserPorile/personal.html", {"form": form})


@login_required
def address(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = AddressForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Address info saved.")
            return redirect("profile:professional")
    else:
        form = AddressForm(instance=profile)
    return render(request, "UserPorile/address.html", {"form": form})


@login_required
def professional(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = ProfessionalForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Professional info saved.")
            return redirect("profile:payment_bank")
    else:
        form = ProfessionalForm(instance=profile)
    return render(request, "UserPorile/professional.html", {"form": form})


@login_required
def payment_bank(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = PaymentBankForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Banking details saved.")
            return redirect("profile:payment_card")
    else:
        form = PaymentBankForm(instance=profile)
    return render(request, "UserPorile/payment_bank.html", {"form": form})


@login_required
def payment_card(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = PaymentCardForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Card details saved.")
            return redirect("profile:media")
    else:
        form = PaymentCardForm(instance=profile)
    return render(request, "UserPorile/payment_card.html", {"form": form})


@login_required
def media(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = MediaForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Media uploaded.")
            return redirect("profile:review")
    else:
        form = MediaForm(instance=profile)
    return render(request, "UserPorile/media.html", {"form": form})


@login_required
def review(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        # finalise the setup
        profile.setup_completed = True
        profile.save()
        messages.success(request, "Profile setup completed.")
        return redirect("secured:dashboard")
    # show a summary and a form with button to finalize
    return render(request, "UserPorile/review.html", {"profile": profile})
