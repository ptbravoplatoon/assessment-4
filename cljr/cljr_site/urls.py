from django.urls import path
from .views import *

urlpatterns = [
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path("categories/new/", category_new, name="category_new"),
    path("categories/<int:category_id>", category_detail, name="category_detail"),
    path("categories/<int:category_id>/edit", category_edit, name="category_edit"),
    path("categories/<int:category_id>/delete", category_delete, name="category_delete"),

    path("categories/<int:category_id>/posts/new/", PostCreateView.as_view(), name="post_new"),
    path("categories/<int:category_id>/posts/<int:post_id>/", PostDetailView.as_view(), name="post_detail"),
    path("categories/<int:category_id>/posts/<int:post_id>/edit", PostUpdateView.as_view(), name="post_edit"),
    path("categories/<int:category_id>/posts/<int:post_id>/delete", PostDeleteView.as_view(), name="post_delete")
]