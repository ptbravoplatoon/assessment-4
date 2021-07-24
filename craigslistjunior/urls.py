from django.urls import path, include
from .views import *
urlpatterns = [
    path('', home,name="home"),
    path('categories',categories_list,name='categories_list'),
    path('categories/<category_id>',posts_by_categories,name='posts_by_categories'),
    path('category/new',add_categories,name='add_categories'),
    path('categories/<category_id>/edit',edit_categories,name='edit_categories'),
    path('categories/<category_id>/delete',delete_categories,name='delete_categories'),
    path('categories/<category_id>/posts/new',add_new_post,name='add_new_post'),
    path('categories/<category_id>/posts/<post_id>',post_details,name='post_details'),
    path('categories/<category_id>/posts/<post_id>/edit',edit_post_details,name='edit_post_details'),
    path('categories/<category_id>/posts/<post_id>/delete',delete_post_details,name='delete_post_details'),
]