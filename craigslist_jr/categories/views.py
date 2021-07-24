from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from .models import Category, Post
from .forms import CategoryForm, PostForm

class AllCategoriesView(ListView):
    model = Category
    template_name = "all_categories.html"
    context_object_name = "categories"
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "All Categories"
        return context

class NewCategoryView(View):
    def get(self, request):
        form = CategoryForm()
        context = {'form':form}
        return render(request, 'new_category.html', context) #form template
    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse('categories:all_categories'))

class CategoryView(View):
    def get(self, request, cat_id):
        try:
            cat = Category.objects.get(id=cat_id)
            posts = []
            try:
                posts = Post.objects.filter(category=cat_id)
            except:
                pass
            context = {'item':cat, 'posts': posts}
            return render(request, 'category_details.html', context)
        except Exception as e:
            print(e)
            return redirect(reverse('categories:all_categories'))

class EditCategoryView(View):
    def get(self, request, cat_id):
        try:
            cat = Category.objects.get(id=cat_id)
        except Exception as e:
            print(e)
            return redirect(reverse('categories:all_categories'))
        form = CategoryForm(instance=cat)
        context = {'form':form}
        return render(request, 'new_category.html', context)
    
    def post(self, request, cat_id):
        try:
            cat = Category.objects.get(id=cat_id)
        except Exception as e:
            print(e)
            return redirect(reverse('categories:all_categories'))
        form = CategoryForm(request.POST, instance=cat)
        if form.is_valid():
            form.save()
        return redirect(reverse('categories:view_category', args=[cat_id]))

class DeleteCategoryView(View):
    def get(self, request, cat_id):
        Category.objects.filter(id=cat_id).delete()
        return redirect(reverse('categories:all_categories'))

#---------------------------------------------------------------
class NewPostView(View):
    def get(self, request, cat_id):
        form = PostForm()
        print(form.fields.keys())
        form.fields['category'].initial = cat_id
        context = {'form':form}
        return render(request, 'new_post.html', context) #form template
    def post(self, request, cat_id):
        form = PostForm(request.POST)        
        if form.is_valid():
            form.save()
        return redirect(reverse('categories:view_category', args=[cat_id]))

class PostView(View):
    def get(self, request, cat_id, post_id):
        try:
            post = Post.objects.get(id=post_id)
            context = {'item':post}
            return render(request, 'post_details.html', context)
        except:
            return redirect(reverse('categories:view_category', args=[cat_id]))

class EditPostView(View):
    def get(self, request, cat_id, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except Exception as e:
            print(e)
            return redirect(reverse('categories:view_category', args=[cat_id]))
        form = PostForm(instance=post)
        context = {'form':form}
        return render(request, 'new_post.html', context)
    
    def post(self, request, cat_id, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except Exception as e:
            print(e)
            return redirect(reverse('categories:view_category', args=[cat_id]))
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return redirect(reverse('categories:view_post', args=[cat_id, post_id]))

class DeletePostView(View):
    def get(self, request, cat_id, post_id):
        Post.objects.filter(id=post_id).delete()
        return redirect(reverse('categories:view_category', args=[cat_id]))
