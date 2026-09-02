from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_post", views.create_post, name="create_post"),
    path("my_posts", views.user_posts, name="my_posts"),
    path("delete_post/<int:pk>", views.delete_post, name="delete_post"),
]