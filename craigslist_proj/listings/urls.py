from django.urls import path
from .views import *

urlpatterns = [
    path('', ListCategories.as_view(), name='list_categories'),
    # A page listing all the categories
    path('new/', NewCategory.as_view(), name='new_category'),
    # A page with a form to create a new category
    path('<int:category_id>', category_detail, name='category_detail'),
    # A page to view the detail of a specific category and a list of all of its associated posts
    path('<int:category_id>/edit', edit_category, name='edit_category'),
    # A page with a form to update a specific category, with current values filled in already. Also include the ability to delete the specific category here.
    path('<int:category_id>/delete', delete_category, name='delete_category'),
    # A page with a form to delete the specific category here.
    # --------POSTS
    path('<int:category_id>/posts/new', NewPost.as_view(), name='new_post'),
    # A page with a form to create a new post, under the current category by default.

    path('<int:category_id>/posts/<int:post_id>', post_detail, name='post_detail'),
    # A page to view the detail of a specific post. Also include the ability go back to the parent category detail page (/categories/:category_id/)

    path('<int:category_id>/posts/<int:post_id>/edit', edit_post, name='edit_post'),
    # A page with a form to update a specific post, with current values filled in already. Also include the ability to delete the specific post here.

    path('<int:category_id>/posts/<int:post_id>/delete', delete_post, name='delete_post'),
    # A page with a form to delete the specific post here.
]
