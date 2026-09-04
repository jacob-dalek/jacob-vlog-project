from django.contrib import admin
from app.models import Post, UserProfile, Comment

admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(Comment)