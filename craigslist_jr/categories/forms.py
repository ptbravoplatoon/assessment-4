from django import forms
from django.db.models import fields
from .models import Category, Post

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("title", "description")

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("category","title", "description")