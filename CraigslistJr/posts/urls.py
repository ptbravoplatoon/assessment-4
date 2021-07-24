from django.urls import path
from .views import default, Categories, NewCategory, ViewCategory, EditCategory, DeleteCategory, NewPost, ViewPost, EditPost, DeletePost

urlpatterns = [
    path('', default, name='default'),
    path('categories/', Categories.as_view(), name='categories'),
    path('categories/new/', NewCategory.as_view(), name='new_category'),
    path('categories/<int:category_id>/', ViewCategory.as_view(), name='view_category'),
    path('categories/<int:category_id>/edit/', EditCategory.as_view(), name='edit_category'),
    path('categories/<int:category_id>/delete/', DeleteCategory.as_view(), name='delete_category'),
    path('categories/<int:category_id>/posts/new/', NewPost.as_view(), name='new_post'),
    path('categories/<int:category_id>/posts/<int:post_id>/', ViewPost.as_view(), name='view_post'),
    path('categories/<int:category_id>/posts/<int:post_id>/edit/', EditPost.as_view(), name='edit_post'),
    path('categories/<int:category_id>/posts/<int:post_id>/delete', DeletePost.as_view(), name='delete_post'),
]