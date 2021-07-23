from .models import Category
from .forms import CategoryForm
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

# Category methods
def get_categories(request):
    categories = Category.objects.all()
    return render(request, "craigslist_jr/categories.html", {"categories": categories})


def get_category(request, category_id):
    return HttpResponse("cat_detail")


def new_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cat_all")
    elif request.method == "GET":
        form = CategoryForm()

    return render(request, "craigslist_jr/category_form.html", {"form": form})


def edit_category(request, category_id):
    return HttpResponse("cat_edit")


def delete_category(request, category_id):
    return HttpResponse("cat_delete")


# Post methods
def get_post(request, category_id, post_id):
    return HttpResponse("post_detail")


def new_post(request, category_id):
    return HttpResponse("post_new")


def edit_post(request, category_id, post_id):
    return HttpResponse("post_edit")


def delete_post(request, category_id, post_id):
    return HttpResponse("post_delete")
