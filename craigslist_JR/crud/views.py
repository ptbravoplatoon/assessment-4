from django.shortcuts import render, redirect, HttpResponse

from .forms import CategoryForm, PostForm
from .models import Category, Post

def get_category(category_id):
    return Category.objects.get(id=category_id)

def all_categories(request):
    categories = Category.objects.all()
    return render(request, 'crud/category_list.html', {'categories': categories})

def new_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('category_detail', category_id=category.id)
    else:
        form = CategoryForm()
    return render(request, 'crud/category_form.html', {'form': form, 'type_of_request': 'New'})


def category_detail(request, category_id):
    category = get_category(category_id)
    posts = category.posts.all()
    return render(request, 'crud/category_detail.html', {'category': category, 'posts': posts})

def edit_category(request, category_id):
    category = get_category(category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('category_detail', category_id=category.id)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'crud/category_form.html', {'form': form, 'type_of_request': 'Edit'})

def delete_category(request, category_id):
    if request.method == "POST":
        category = get_category(category_id)  
        category.delete()
    return redirect('all_categories')

def get_post(post_id):
    return Post.objects.get(id=post_id)


def new_post(request, category_id):
    category = get_category(category_id)

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', category_id=post.category.id, post_id=post.id)
    else:
        form = PostForm()
    return render(request, 'crud/post_form.html', {'form': form, 'type_of_request': 'New'})



def post_detail(request, category_id, post_id):
    category = get_category(category_id)
    post = get_post(post_id)
    return render(request, 'crud/post_detail.html', {'category': category, 'post': post})

def edit_post(request, category_id, post_id):
    category = get_category(category_id)
    post = get_post(post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', post_id=post.id, category_id=category_id)
    else:
        form = PostForm(instance=post)
    return render(request, 'crud/post_form.html', {'form': form, 'type_of_request': 'Edit'})

def delete_post(request, category_id, post_id):
    if request.method == "POST":
        post = get_post(post_id)
        post.delete()
    return redirect('category_detail', category_id=category_id)

