from django.urls import path, include
from .views import *

app_name = "categories"

urlpatterns = [
    path('', AllCategoriesView.as_view(), name='all_categories'),
    path('new/', NewCategoryView.as_view(), name='new_category'),
    path('<int:cat_id>/', CategoryView.as_view(), name='view_category'),
    path('<int:cat_id>/edit/', EditCategoryView.as_view(), name='edit_category'),
    path('<int:cat_id>/delete/', DeleteCategoryView.as_view(), name='delete_category'),
    path('<int:cat_id>/posts/new/', NewPostView.as_view(), name='new_post'),
    path('<int:cat_id>/posts/<int:post_id>/', PostView.as_view(), name='view_post'),
    path('<int:cat_id>/posts/<int:post_id>/edit/', EditPostView.as_view(), name='edit_post'),
    path('<int:cat_id>/posts/<int:post_id>/delete/', DeletePostView.as_view(), name='delete_post')
]