from django.shortcuts import render, redirect, reverse
from .models import *
from .forms import CategoryForm, PostForm
import os

def list_categories(request):
    categories = Category.objects.all()
    context = {
        "categories": categories
    }
    return render(request, 'listings/list_categories.html', context)

def new_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("list_categories"))
    if request.method == "GET":
        form = CategoryForm()
        return render(request, "listings/new_category.html", {"form": form})

def category_detail(request,category_id):
    category = Category.objects.get(pk=category_id)
    posts = category.posts.all()
    context = {
        "category": category,
        "posts": posts  
    }
    return render(request, 'listings/category_detail.html', context)

def edit_category(request,category_id):
    obj = Category.objects.get(pk=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("category_detail",category_id=category_id)
    if request.method == "GET":
        form = CategoryForm(instance=obj)
        return render(request, 'listings/edit_category.html', {'form': form, 'type_of_request': 'Edit', "category_id": category_id})

def delete_category(request,category_id):
    obj = Category.objects.get(pk=category_id)
    if request.method == "POST":
        obj.delete()
        return redirect("list_categories")
    if request.method == "GET":
        return render(request, "listings/delete_category.html", {"name": obj.topic, "category_id": category_id})

def new_post_listing_for_category(request,category_id):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("category_detail",category_id=category_id)
    if request.method == "GET":
        form = PostForm(initial={'category': category_id})
        #form.fields['category'].widget.attrs['readonly'] = True 
        return render(request, "listings/new_post_listing_for_category.html", {"form": form})
    
def post_detail_for_category(request,category_id,post_id):
    post = Post.objects.get(pk=post_id)
    context = {
        "post": post,
        "category_id": category_id
    }
    return render(request, 'listings/post_detail_for_category.html', context)

def edit_post_for_category(request,category_id,post_id):
    obj = Post.objects.get(pk=post_id)
    if request.method == "POST":
        form = PostForm(request.POST or None, request.FILES or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("post_detail_for_category",category_id=category_id,post_id=post_id)
    if request.method == "GET":
        form = PostForm(instance=obj)
        return render(request, "listings/edit_post_for_category.html", {"form": form, "category_id": category_id, "post_id": post_id, 'type_of_request': 'Edit'})

def delete_post_for_category(request,category_id,post_id):
    obj = Post.objects.get(pk=post_id)
    if request.method == "POST":
        obj.delete()
        return redirect("category_detail", category_id=category_id)
    if request.method == "GET":
        return render(request, "listings/delete_post_for_category.html", {"name": obj.title, "category_id": category_id})


