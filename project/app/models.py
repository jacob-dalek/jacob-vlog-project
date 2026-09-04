from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=128, blank=True)
    can_post = models.BooleanField(default=False) # needs to be authorized by an admin

    def get_username(self):
        return self.user.username

    def __str__(self):
        return f"{self.get_username()}"




class Post(models.Model):

    title = models.CharField(name="Title", blank=False) # may need to reconsider constructor args
    desc = models.TextField(name="Description", 
                            blank=False, 
                            max_length=500,
                            )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __repr__(self):
        return f"{self.Title}"
    
    def __str__(self):
        return  f"{self.Title}"

class Comment(models.Model):
    comment = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
