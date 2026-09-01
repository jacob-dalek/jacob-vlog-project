from django.forms import ModelForm
from app.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "desc"]