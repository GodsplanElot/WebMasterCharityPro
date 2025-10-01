from django.shortcuts import redirect
from functools import wraps

def verified_and_profile_complete_required(
    redirect_to="accounts:not_verified", profile_wizard="profile:wizard_start"
):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect("accounts:login")
            # ensure profile exists
            profile = getattr(request.user, "profile", None)
            if profile is None:
                # create redirect or create profile automatically
                return redirect(profile_wizard)
            if not profile.completed:
                # force user to complete profile first
                return redirect(profile_wizard)
            if not profile.is_verified:  # <-- fixed field name
                return redirect(redirect_to)
            return view_func(request, *args, **kwargs)
        return _wrapped
    return decorator
