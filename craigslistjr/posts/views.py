from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Category, Post
from django.utils import timezone
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

class CategoryListView(ListView):
    model = Category
    ordering = ['name']
    context_object_name = 'categories'

class CategoryCreateView(CreateView):
    model = Category
    fields = ['name', 'description']
    success_url = reverse_lazy('category_list')

    def form_valid(self, form):
        form.instance.date_created = timezone.now()
        return super().form_valid(form)

class CategoryDetailView(DetailView):
    model = Category
    pk_url_kwarg = 'category_id'
    context_object_name = 'category'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        post_list = Post.objects.filter(category__id=self.kwargs['category_id'])
        context['post_list'] = post_list
        return context

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'description']
    template_name_suffix = '_update_form'
    pk_url_kwarg = 'category_id'

    def get_success_url(self):
        category_id = self.kwargs['category_id']
        return reverse_lazy('category_detail', kwargs={'category_id': category_id})

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('category_list')
    pk_url_kwarg = 'category_id'

# class PostListView(ListView):
#     model = Post
#     ordering = ['date_created']
#     context_object_name = 'posts'

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context['category_id'] = self.kwargs['category_id']
#         return context

#     def get_queryset(self):
#         category_id = self.kwargs['category_id']
#         return Post.objects.filter(category__id=category_id)

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.date_created = timezone.now()
        form.instance.last_edit = timezone.now()
        form.instance.category = Category.objects.get(pk=self.kwargs['category_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('category_detail', kwargs={'category_id': self.kwargs['category_id']})

class PostDetailView(DetailView):
    model = Post
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'

    def get_object(self):
        post_id = self.kwargs['post_id']
        return Post.objects.get(pk=post_id)

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name_suffix = '_update_form'
    pk_url_kwarg = 'post_id'

    def form_valid(self, form):
        form.instance.last_edit = timezone.now()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'category_id': self.kwargs['category_id'], 'post_id': self.kwargs['post_id']})

class PostDeleteView(DeleteView):
    Model = Post
    pk_url_kwarg = 'post_id'

    def get_object(self):
        post_id = self.kwargs['post_id']
        return Post.objects.get(pk=post_id)

    def get_success_url(self):
        return reverse_lazy('category_detail', kwargs={'category_id': self.kwargs['category_id']})