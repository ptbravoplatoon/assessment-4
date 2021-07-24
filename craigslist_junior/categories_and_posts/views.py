from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from .models import Category, Post
from .forms import CategoryForm, PostForm

def get_category(category_id):
    return Category.objects.get(id=category_id)

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories_and_posts/category_list.html', {'categories':categories})

def category_detail(request, category_id):
    category = get_category(category_id)
    posts = category.posts.all()
    return render(request, 'categories_and_posts/category_detail.html', {'category': category, 'posts': posts})

def new_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('category_detail', category_id=category.id)
    else:
        form = CategoryForm()
    return render(request, 'categories_and_posts/category_form.html', {'form': form, 'type_of_request': 'New'})

def edit_category(request, category_id):
    category = get_category(category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            try:
                category = form.save(commit=False)
                category.save()
                return redirect('category_detail', category_id=category.id)
            except:
                error_message = 'Something went wrong.'
                return render(request, 'categories_and_posts/category_form.html', {'form': form, 'type_of_request': 'Edit', 'error_message': error_message})
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories_and_posts/category_form.html', {'form': form, 'type_of_request': 'Edit'})

def delete_category(request, category_id):
    category = get_category(category_id)  
    if request.method == "POST":
        try:
            category.delete()
            return redirect(reverse('category_list'))
        except:
            error_message = 'Something went wrong.'
            return render(request, 'categories_and_posts/category_delete.html', {'name': category.title, 'error_message': error_message})
    if request.method == "GET":
        return render(request, 'categories_and_posts/category_delete.html', {'name': category.title})

def get_post(post_id):
    return Post.objects.get(id=post_id)

def post_list(request, category_id):
    category = get_category(category_id)
    posts = category.posts.all()
    return render(request, 'categories_and_posts/post_list.html', {'category': category, 'posts': posts})

def post_detail(request, category_id, post_id):
    category = get_category(category_id)
    post = get_post(post_id)
    return render(request, 'categories_and_posts/post_detail.html', {'category': category, 'post': post})

def new_post(request, category_id):
    category = get_category(category_id)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', category_id=post.category.id, post_id=post.id)
    else:
        form = PostForm(initial={'category': category.id})
    return render(request, 'categories_and_posts/post_form.html', {'form': form, 'type_of_request': 'New'})

def edit_post(request, category_id, post_id):
    category = get_category(category_id)
    post = get_post(post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            try:
                post = form.save(commit=False)
                post.save()
                return redirect('post_detail', post_id=post.id, category_id=category.id)
            except:
                error_message = 'Something went wrong.'
                (request, 'categories_and_posts/post_form.html', {'form': form, 'type_of_request': 'Edit', 'error_message': error_message})
    else:
        form = PostForm(instance=post)
    return render(request, 'categories_and_posts/post_form.html', {'form': form, 'type_of_request': 'Edit'})

def delete_post(request, category_id, post_id):
    category = get_category(category_id)
    post = get_post(post_id)
    if request.method == "POST":
        try:
            post.delete()
            return redirect('category_detail', category_id=category.id)
        except:
            error_message = 'Something went wrong.'
            return render(request, 'categories_and_posts/post_delete.html', {'name': post.title, 'error_message': error_message})
    if request.method == "GET":
        return render(request, 'categories_and_posts/post_delete.html', {'name': post.title})
