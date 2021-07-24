from django.urls import path
from . import views



urlpatterns = [
    #list all categories
    path('', views.all_categories, name='all_categories'),
    #create new category
    path('new', views.new_category, name='new_category'),
    #view individual category with a list of all its post
    path('<int:category_id>', views.category_detail, name='category_detail'),
    #update/delete individual category
    path('<int:category_id>/edit', views.edit_category, name='edit_category'),
    #update/delete individual category
    path('<int:category_id>/delete', views.delete_category, name='delete_category'),
    #create nested post
    path('<int:category_id>/posts/new', views.new_post, name='new_post'),
    #view post detail, add button to navigate back to parent category
    path('<int:category_id>/posts/<int:post_id>', views.post_detail, name='post_detail'),
    #edit/delete post detail
    path('<int:category_id>/posts/<int:post_id>/edit', views.edit_post, name='edit_post'),
    #edit/delete post detail
    path('<int:category_id>/posts/<int:post_id>/delete', views.delete_post, name='delete_post'),

]