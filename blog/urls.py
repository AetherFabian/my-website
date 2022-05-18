from django import views
from django.urls import path
from .views import render_posts, post_detail

urlpatterns = [
    path('', render_posts, name='posts'),
    path("post/<int:post_id>", post_detail)
]