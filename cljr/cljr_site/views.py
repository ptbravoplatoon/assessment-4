from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView

from .models import *
from .forms import *

class CategoryListView(ListView):
    model = Category
    template_name = "cljr_site/category_list.html"
    context_object_name = "categories"

def category_new(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("category_list")
    else:
        form = CategoryForm()
    return render(request, "cljr_site/category_form.html", {"form": form, "type_of_request": "New"})

def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    posts = Post.objects.filter(category=category)
    return render(request, "cljr_site/category_detail.html", {"category": category, "posts": posts})

def category_edit(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("category_detail", category_id=category_id)
    else:
        form = CategoryForm(instance=category)
    return render(request, "cljr_site/category_form.html", {"form": form, "type_of_request": "Edit"})

def category_delete(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == "POST":
        category.delete()
        return redirect("category_list")
    else:
        return render(request, "cljr_site/category_delete.html", {"category": category})








class PostCreateView(CreateView):
    model = Post
    template_name = "cljr_site/post_new.html"
    fields = ["title", "text"]

    def form_valid(self, form):
        temp_form = form.save(commit=False)
        temp_form.category = Category.objects.get(pk=self.kwargs["category_id"])
        return super().form_valid(temp_form)

    def get_success_url(self):
        return reverse_lazy("category_detail", kwargs = {"category_id": self.kwargs["category_id"]})

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["type_of_request"] = "New"
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = "cljr_site/post_detail.html"
    pk_url_kwarg = "post_id"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        category_id = self.kwargs["category_id"]
        category = Category.objects.get(id=category_id)
        context["category"] = category
        return context

    def get_object(self):
        post_id = self.kwargs["post_id"]
        return Post.objects.get(pk=post_id)

class PostUpdateView(UpdateView):
    model = Post
    template_name = "cljr_site/post_new.html"
    fields = ["title", "text"]
    pk_url_kwarg = "post_id"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["type_of_request"] = "Edit"
        return context

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs = {"category_id": self.kwargs["category_id"], "post_id": self.kwargs["post_id"]})

class PostDeleteView(DeleteView):
    model = Post
    pk_url_kwarg = "post_id"

    
    def get_success_url(self):
        return reverse_lazy("category_detail", kwargs = {"category_id": self.kwargs["category_id"]})
