
from app.models import UserProfile
from django.shortcuts import redirect


def user_can_post(func):
  def wrapper(request, *args, **kwargs):
    user_profile = UserProfile.objects.get(user=request.user) # assuming user is already verified
    if (not user_profile.can_post):
      return redirect("index")
    else:
      return function(request, *args, **kwargs)

  return wrapper
