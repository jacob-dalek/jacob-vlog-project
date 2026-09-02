from django.shortcuts import render
from app.forms import PostForm
from app.models import Post, UserProfile
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from app.decorators import user_can_post
from django.views.decorators.http import require_http_methods

def index(request):
    return render(request, "app/index.html")

@login_required
# @user_can_post # custom decorator 
def create_post(request):

    current_user = User.objects.get(id=request.user.id)
    UserProfile.objects.get_or_create(user=current_user) # create user_profile instance  

    context = {}
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
             new_post = form.save(commit=False)
             new_post.user_id = UserProfile.objects.get(user=current_user).id
             form.save()
             return render(request, "app/create_post.html#success-message", context)

    context["form"] = form

    return render(request, "app/create_post.html", context)

@login_required
def user_posts(request):
    pass