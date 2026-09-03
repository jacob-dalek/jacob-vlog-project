from django.shortcuts import get_object_or_404, render
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


    context = {}
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
             new_post = form.save(commit=False)
             new_post.user_id = request.user.userprofile.id
             form.save()
             context["message"] = f"{new_post.Title} Successfully Created!"
             return render(request, "app/create_post.html#alert", context)

    context["form"] = form

    return render(request, "app/create_post.html", context)

@login_required
def user_posts(request):
    context = {}
    post_arr = Post.objects.filter(user=request.user.userprofile).all()
    context["post_arr"] = post_arr

    # if not post_arr:
    #     return render(request, "app/user_posts.html#no_posts", context)


    return render(request, "app/user_posts.html", context)

@login_required
@require_http_methods(["DELETE"])
def delete_post(request, pk):
    context = {}
    post = get_object_or_404(Post, pk=pk, user=request.user.userprofile)
    post.delete()
    context["message"] = f"{post.Title} Successfully Deleted!"

    return render(request, "app/user_posts.html#post_list", context)

def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk, user=request.user.userprofile)
    if request.method == "POST":
        form = Post(request.POST, instance=post)
        if form.is_valid():
            form.save()

    context = {
        "form": Post(instance=post),
        "post": post
    }
    
    return render(request, "app/user_posts.html#update_post", context)




