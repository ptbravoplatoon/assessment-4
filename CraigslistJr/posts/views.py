from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Category, Post


def default(request):
    return redirect(reverse_lazy('categories'))

class Categories(ListView):
    model = Category
    template_name = "posts/categories.html"
    context_object_name = "categories"

class NewCategory(CreateView):
    model = Category
    template_name = "posts/new_category.html"
    fields = ["name"]
    success_url = reverse_lazy('categories')

class ViewCategory(DetailView):
    model = Category
    template_name = "posts/view_category.html"
    context_object_name = "category"
    pk_url_kwarg = 'category_id'

    def get_context_data(self, *args, **kwargs):
        context = super(ViewCategory, self).get_context_data(*args, **kwargs)
        category_id = self.kwargs["category_id"]
        context["posts"] = Post.objects.filter(category__id=category_id)
        return context

class EditCategory(UpdateView):
    model = Category
    template_name = "posts/edit_category.html"
    fields = ["name"]
    pk_url_kwarg = 'category_id'

    def get_success_url(self):
        category_id = self.kwargs["category_id"]
        return reverse('view_category', kwargs={'category_id':category_id})

class DeleteCategory(DeleteView):
    model = Category
    template_name = "posts/delete_category.html"
    context_object_name = "category"
    success_url = reverse_lazy('categories')
    pk_url_kwarg = 'category_id'

class NewPost(CreateView):
    model = Post
    template_name = "posts/new_post.html"
    fields = ["title", "description"]
    pk_url_kwarg = 'category_id'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        category_id = self.kwargs["category_id"]
        context["category"] = Category.objects.get(id=category_id)
        return context

    def form_valid(self, form):
        form = form.save(commit=False)
        category_id = self.kwargs["category_id"]
        form.category = Category.objects.get(id=category_id)
        return super().form_valid(form)
    
    def get_success_url(self):
        category_id = self.kwargs["category_id"]
        return reverse_lazy('view_category', kwargs={'category_id':category_id})

class ViewPost(DetailView):
    model = Post
    template_name = "posts/view_post.html"
    context_object_name = "post"
    pk_url_kwarg = 'post_id'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        category_id = self.kwargs["category_id"]
        context["category"] = Category.objects.get(id=category_id)
        return context

class EditPost(UpdateView):
    model = Post
    template_name = "posts/edit_post.html"
    fields = ["title", "description"]
    pk_url_kwarg = 'post_id'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        category_id = self.kwargs["category_id"]
        context["category"] = Category.objects.get(id=category_id)
        return context

    def get_success_url(self):
        category_id = self.kwargs["category_id"]
        post_id = self.kwargs["post_id"]
        return reverse_lazy('view_post', kwargs={'category_id':category_id, 'post_id':post_id})

class DeletePost(DeleteView):
    model = Post
    template_name = "posts/delete_post.html"
    context_object_name = "post"
    pk_url_kwarg = 'post_id'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        category_id = self.kwargs["category_id"]
        context["category"] = Category.objects.get(id=category_id)
        return context

    def get_success_url(self):
        category_id = self.kwargs["category_id"]
        return reverse_lazy('view_category', kwargs={'category_id':category_id})