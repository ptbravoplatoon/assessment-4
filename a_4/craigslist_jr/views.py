from django.http.response import HttpResponse
from django.shortcuts import render

# Category methods
def get_categories(request):
    return HttpResponse("cat_all")


def get_category(request, category_id):
    return HttpResponse("cat_detail")


def new_category(request):
    return HttpResponse("cat_new")


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
