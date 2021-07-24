from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoriesListView.as_view(), name="cat_list"), # list all the categories
    path('categories/new', CategoriesNewView.as_view(), name="cat_create"), # create a new category
    path('categories/<int:category_id>/', CategoriesDetailView.as_view(), name="cat_detail"), # List all associated posts
    path('categories/<int:category_id>/edit/', CategoriesEditView.as_view(), name="cat_edit"), # edit a category (also delete)
    path('categories/<int:category_id>/delete/', CategoriesDeleteView.as_view(), name="cat_delete"),  # delete a category
    path('categories/<int:category_id>/posts/new/', PostsNewView.as_view(), name="post_create"), # create a new post under current category
    path('categories/<int:category_id>/posts/<int:post_id>/', PostDetailView.as_view(), name="post_detail"), # view the detail of a post
    path('categories/<int:category_id>/posts/<int:post_id>/edit/', PostEditView.as_view(), name="post_edit"), # edit a post (also delete)
    path('categories/<int:category_id>/posts/<int:post_id>/delete/', PostDeleteView.as_view(), name="post_delete"), # delete a post
]