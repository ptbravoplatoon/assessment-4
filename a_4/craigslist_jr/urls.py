from django.urls import path
from .views import (
    get_categories,
    get_category,
    new_category,
    edit_category,
    delete_category,
    new_post,
    get_post,
    edit_post,
    delete_post,
)

urlpatterns = [
    path("", get_categories, name="cat_all"),
    path("categories/", get_categories, name="cat_all"),
    path("categories/new/", new_category, name="cat_new"),
    path("categories/<int:category_id>/", get_category, name="cat_detail"),
    path("categories/<int:category_id>/edit/", edit_category, name="cat_edit"),
    path("categories/<int:category_id>/delete/", delete_category, name="cat_delete"),
    path("categories/<int:category_id>/posts/new/", new_post, name="post_new"),
    path(
        "categories/<int:category_id>/posts/<int:post_id>/",
        get_post,
        name="post_detail",
    ),
    path(
        "categories/<int:category_id>/posts/<int:post_id>/edit/",
        edit_post,
        name="post_edit",
    ),
    path(
        "categories/<int:category_id>/posts/<int:post_id>/delete/",
        delete_post,
        name="post_delete",
    ),
]
