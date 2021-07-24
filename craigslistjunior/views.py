from django.shortcuts import render , redirect
from .models import *
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html')
def categories_list(request):
    context = {}
    context['categories'] = Category.objects.order_by('id').all()
    return render(request,'categories.html',context)
def add_categories(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        descr = request.POST.get('description')
        Category.objects.create(name=name,description=descr)
        messages.success(request,"Successfully created new category")
        return redirect("/categories")
    return render(request,'add-category.html')
def    edit_categories(request,category_id):
    context = {}
    category = Category.objects.get(id=category_id)
    context['category'] = category
    if request.method == 'POST':
        category.name = request.POST.get('name')
        category.description = request.POST.get('description')
        category.save()
        messages.success(request,"Successfully updated category")
        return redirect("/categories")

    return render(request,'edit-category.html',context)
def delete_categories(request,category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    messages.warning(request,"Deleted your category")
    return redirect("/categories")
def    posts_by_categories(request,category_id):
    context = {}
    category= Category.objects.get(id=category_id)
    context['category']  = category
    context['posts'] = Post.objects.filter(category_id=category).order_by('id').all()
    return render(request,'posts.html',context)
def add_new_post(request,category_id):
    context = {}
    category= Category.objects.get(id=category_id)
    context['category']  = category 
    if request.method == 'POST':
        Post.objects.create(title=request.POST.get("title"),short_description=request.POST.get('description'),content=request.POST.get('content'),category_id=category)
        messages.success(request,"Successfully added new post")
        return redirect("/categories/"+str(category.id))
    return render(request,'add-new-post.html',context)
def     post_details(request,category_id,post_id):
    context = {}
    category= Category.objects.get(id=category_id)
    context['category']  = category
    context['post'] = Post.objects.get(id=post_id)
    return render(request,'post-detail.html',context)
def   edit_post_details(request,category_id,post_id):
    context = {}
    category= Category.objects.get(id=category_id)
    context['category']  = category
    post = Post.objects.get(id=post_id)
    context['post'] = post
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.short_description = request.POST.get('description')
        post.content = request.POST.get('content')
        post.save()
        return redirect("/categories/"+str(category.id))
    return render(request,'edit-post-detail.html',context)
def  delete_post_details(request,category_id,post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    category= Category.objects.get(id=category_id)
    messages.warning(request,"Deleted your post")
    return redirect("/categories/"+str(category.id))