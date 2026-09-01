from django.shortcuts import render
from app.forms import PostForm

def index(request):
    return render(request, "app/index.html")

def upload_post(request):
    ...