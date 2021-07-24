from django.urls import path
from .views import CategoryListView, CategoryCreateView, CategoryDetailView, CategoryUpdateView, CategoryDeleteView
from .views import PostCreateView, PostDetailView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', CategoryListView.as_view(), name='category_list'),
    path('new/', CategoryCreateView.as_view(), name='category_create'),
    path('<int:category_id>/', CategoryDetailView.as_view(), name='category_detail'),
    path('<int:category_id>/edit/', CategoryUpdateView.as_view(), name='category_update'),
    path('<int:category_id>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
    path('<int:category_id>/posts/new/', PostCreateView.as_view(), name='post_create'),
    path('<int:category_id>/posts/<int:post_id>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:category_id>/posts/<int:post_id>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('<int:category_id>/posts/<int:post_id>/delete', PostDeleteView.as_view(), name='post_delete'),

]
