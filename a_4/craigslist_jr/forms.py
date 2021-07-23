from django.db.models.base import Model
from django.forms import ModelForm
from .models import Category, Post


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        exclude = ["id"]


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ["id"]
