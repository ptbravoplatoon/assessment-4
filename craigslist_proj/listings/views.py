from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from .models import Category, Post
from .forms import CategoryForm, PostForm
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy


class ListCategories(ListView):
    model = Category
    queryset = Category.objects.all()
    context_object_name = "categories"
    template_name = "listings/list_categories.html"

class NewCategory(CreateView):
    model = Category
    template_name = "listings/new_category.html"
    form_class = CategoryForm
    success_url = "/categories/"

def category_detail(request, category_id):
    category = Category.objects.get(pk=category_id)
    cat_posts = category.posts.all()
    context = {'category':category, "cat_posts":cat_posts}
    return render(request, 'listings/category_detail.html', context)

def edit_category(request, category_id):
    catobj = Category.objects.get(pk=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=catobj) 
        if form.is_valid():
            catobj = form.save(commit=False)
            catobj.save()
            return redirect('category_detail', category_id=category_id)
        else:
            message="Invalid form entry. Please try again."
            return render(request, 'listings/edit_category.html', {"form":form, "catobj":catobj, "invalid_form_message":message})

    if request.method == "GET":
        form = CategoryForm(instance=catobj)
        return render(request, 'listings/edit_category.html', {"form":form, "catobj":catobj})


def delete_category(request, category_id):
    if request.method == "POST":
        catobj = Category.objects.get(pk=category_id)  
        catobj.delete()
        return redirect('list_categories')
    if request.method == "GET":
        catobj = Category.objects.get(pk=category_id)
        return render(request, 'listings/delete_category.html', {"catobj":catobj})
    

class NewPost(CreateView):
    model = Post
    template_name = "listings/new_post.html"
    form_class = PostForm

    def form_valid(self, form):
        form = form.save(commit = False)
        form.category = Category.objects.get(pk=self.kwargs["category_id"])
        return super().form_valid(form)
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["category"] = Category.objects.get(pk=self.kwargs["category_id"])
        context["message"] = "My-Context-Message"
        return context

    def get_success_url(self):
        return reverse_lazy('category_detail', kwargs={"category_id": self.kwargs["category_id"]})

def post_detail(request, category_id, post_id):
    post = Post.objects.get(pk=post_id)
    category = Category.objects.get(pk=category_id)
    context = {'post':post, 'category':category}
    return render(request, 'listings/post_detail.html', context)

def edit_post(request, category_id, post_id):
    post = Post.objects.get(pk=post_id)
    category = Category.objects.get(pk=category_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post) 
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect(reverse('post_detail', kwargs={'post_id':post.pk, 'category_id':category.pk}))
        else:
            message="Invalid form entry. Please try again."
            return render(request, 'listings/edit_post.html', {"form":form, "post":post, "invalid_form_message":message})
    if request.method == "GET":
        form = PostForm(instance=post)
        return render(request, 'listings/edit_post.html', {"form":form, "post":post, "category":category})


def delete_post(request, category_id, post_id):
    if request.method == "POST":
        post = Post.objects.get(pk=post_id)
        category = Category.objects.get(pk=category_id)   
        post.delete()
        return redirect(reverse('category_detail', kwargs={'category_id':category.pk}))
        # return redirect(reverse('post_detail', kwargs={'post_id':post.pk, 'category_id':category.pk}))
    if request.method == "GET":
        post = Post.objects.get(pk=post_id)
        category = Category.objects.get(pk=category_id)  
        return render(request, 'listings/delete_post.html', {"category":category, "post":post})
