from django.urls import path
from .views import list_categories, new_category, category_detail,edit_category,delete_category,post_listing_for_category,new_post_listing_for_category,post_detail_for_category,edit_post_for_category,delete_post_for_category

urlpatterns = [
    path('', list_categories, name="list_categories"),
    path('new/', new_category, name="new_category"),
    path('<int:category_id>/', category_detail, name="category_detail"),
    path('<int:category_id>/edit', edit_category, name="edit_category"),
    path('<int:category_id>/delete', delete_category, name="delete_category"),
    path('<int:category_id>/posts/', post_listing_for_category, name="post_listing_for_category"),
    path('<int:category_id>/posts/new', new_post_listing_for_category, name="new_post_listing_for_category"),
    path('<int:category_id>/posts/<int:post_id>', post_detail_for_category, name="post_detail_for_category"),
    path('<int:category_id>/posts/<int:post_id>/edit', edit_post_for_category, name="edit_post_for_category"),
    path('<int:category_id>/posts/<int:post_id>/delete', delete_post_for_category, name="delete_post_for_category")
]