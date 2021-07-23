from django.shortcuts import render, redirect, reverse
from .models import Category, Post
from .forms import CategoryForm, PostForm

def get_category(category_id):
    return Category.objects.get(id=category_id)

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/category_list.html', {'categories':categories})

def category_new(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('cat_detail', category_id = category.id)
    else:
        form = CategoryForm()
    return render(request, 'categories/category_form.html', {'form': form, 'type_of_request': 'New'})

def category_detail(request, category_id):
    category = get_category(category_id)
    posts = category.posts.all()
    return render(request, 'categories/category_detail.html', {'category': category, 'posts': posts})

def category_edit(request, category_id):
    category = get_category(category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('cat_detail', category_id=category.id)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories/category_form.html', {'form': form, 'type_of_request':'Edit', 'category': category})

def category_delete(request, category_id):
    category = get_category(category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            category.delete()
            return redirect('cat_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories/category_form.html', {'form': form, 'type_of_request':'Delete'})

def get_post(post_id):
    return Post.objects.get(id=post_id)

def post_new(request, category_id):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.category = get_category(category_id)
            post.save()
            return redirect('cat_detail', category_id=post.category.id)
    else:
        form =PostForm()
        category = get_category(category_id)
    return render(request, 'categories/post_form.html', {'form': form, 'type_of_request': 'New', 'category': category})

def post_detail(request, category_id, post_id):
    post = get_post(post_id)
    return render(request, 'categories/post_detail.html', {'post': post})

def post_edit(request, category_id, post_id):
    post = get_post(post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', category_id=post.category.id, post_id=post.id)
    else:
        form = PostForm(instance=post)
        category = get_category(category_id)
    return render(request, 'categories/post_form.html', {'form': form, 'type_of_request': 'Edit', 'category': category, 'post': post})

def post_delete(request, category_id, post_id):
    post = get_post(post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            post.delete()
            return redirect('cat_detail', category_id=post.category.id)
    else:
        form = PostForm(instance=post)
        category = get_category(category_id)
    return render(request, 'categories/post_form.html', {'form': form, 'type_of_request': 'Delete', 'category': category})