from django.urls import path

from blog.views import (
    post_list_view,
    post_detail_view,
    post_like_view,
)

app_name = "blog"

urlpatterns = [

    # POST LIST
    path(
        "posts/",
        post_list_view,
        name="post-list"
    ),

    # POST DETAIL
    path(
        "posts/<slug:slug>/",
        post_detail_view,
        name="post-detail"
    ),

    # POST LIKE
    path(
        "posts/<slug:slug>/like/",
        post_like_view,
        name="post-like"
    ),


]