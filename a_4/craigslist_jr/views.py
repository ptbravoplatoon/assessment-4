from .models import Category, Post
from .forms import CategoryForm, PostForm
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

# Category methods
def get_categories(request):
    categories = Category.objects.all()
    return render(request, "craigslist_jr/categories.html", {"categories": categories})


def get_category(request, category_id):
    category = Category.objects.get(id=category_id)
    return render(request, "craigslist_jr/category.html", {"category": category})


def new_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cat_all")
    elif request.method == "GET":
        form = CategoryForm()

    return render(
        request,
        "craigslist_jr/category_form.html",
        {"form": form, "operation": "Create"},
    )


def edit_category(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("cat_all")
    elif request.method == "GET":
        form = CategoryForm(instance=category)
    return render(
        request,
        "craigslist_jr/category_form.html",
        {"form": form, "operation": "Update", "category": category},
    )


def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == "POST":
        category.delete()
        return redirect("cat_all")
    elif request.method == "GET":
        form = CategoryForm(instance=category)

    return render(
        request,
        "craigslist_jr/category_form.html",
        {"form": form, "operation": "Delete"},
    )


# Post methods
def get_post(request, category_id, post_id):
    post = Post.objects.get(id=post_id)

    return render(request, "craigslist_jr/post.html", {"post": post})


def new_post(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.category = category
            post.save()
            return redirect("cat_detail", category_id=category_id)
    elif request.method == "GET":
        form = PostForm()
    context = {"form": form, "category": category, "operation": "Create"}

    return render(request, "craigslist_jr/post_form.html", context)


def edit_post(request, category_id, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("cat_detail", category_id=category_id)
    elif request.method == "GET":
        form = PostForm(instance=post)

    return render(
        request,
        "craigslist_jr/post_form.html",
        {"form": form, "operation": "Update", "category": post.category, "post": post},
    )


def delete_post(request, category_id, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        post.delete()
        return redirect("cat_detail", category_id=category_id)
    elif request.method == "GET":
        form = PostForm(instance=post)
    return render(
        request,
        "craigslist_jr/post_form.html",
        {"form": form, "operation": "Delete", "category": post.category, "post": post},
    )
