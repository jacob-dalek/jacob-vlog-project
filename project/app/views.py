from django.shortcuts import get_object_or_404, render
from app.forms import PostForm, CommentForm
from app.models import Post, UserProfile, Comment
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
def post_comment(request, pk):
    context = {}
    post = get_object_or_404(Post, pk=pk, user=request.user.userprofile)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user_id = request.user.userprofile.id
            comment.post_id = post.id
            form.save()

            context = {
                            "form": form,
                            "post": post
                        }


            return render(request, "app/user_posts.html#comment_post", context)

    context = {
                                "form": form,
                                "post": post
                            }


    return render(request, "app/user_posts.html#comment_post", context)


@login_required
def user_posts(request):
    context = {}
    post_arr = Post.objects.filter(user=request.user.userprofile).all()
    context["post_arr"] = post_arr
    context["count"] = len(post_arr)

    # print(post_arr[0].comment_set.all())
    
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
    context = {}
    post = get_object_or_404(Post, pk=pk, user=request.user.userprofile)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            context = {
                            "post": post,
                            "message": f"{post.Title} Successfully Updated!"

                        }
            return render(request, "app/user_posts.html#post_updated", context)
            
        else:
            context = {
                "form": PostForm(instance=post),
                "post": post
            }
            return render(request, "app/user_posts.html#update_post", context)

    context = {
                "form": PostForm(instance=post),
                "post": post
            }

    return render(request, "app/user_posts.html#update_post", context)




