from django.shortcuts import render
from app.forms import PostForm
from app.models import Post
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "app/index.html")

@login_required
def create_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
             post = Post(title=form.cleaned_data["title"],
                         desc=form.cleaned_data["desc"],
                         user=request.user)
             post.save()
             return redirect("index")
        else:
            print("ffs")

    return render(request, "app/create_post.html")

    