from django.forms import ModelForm
from app.models import Post, Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class PostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))

    class Meta:
        model = Post
        fields = ["Title", "Description"]

class CommentForm(ModelForm):
    def __init__(self, *args, **kwargs):
            super(CommentForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
    
    class Meta:
        model = Comment
        fields = ["comment"]