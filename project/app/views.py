from django.shortcuts import render
from app.forms import PostForm
from app.models import Post, UserProfile
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "app/index.html")

@login_required
def create_post(request):

    current_user = User.objects.get(id=request.user.id)
    user_profile = UserProfile.objects.get_or_create(user=current_user)

    context = {}
    form = PostForm()
    context["form"] = form
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
             new_post = form.save(commit=False)
             
             new_post.user_id = UserProfile.objects.get(user=current_user).id
             print(new_post.user)
             form.save()


            #  return redirect("index")
        else:
            print("ffs")

    return render(request, "app/create_post.html", context)

    