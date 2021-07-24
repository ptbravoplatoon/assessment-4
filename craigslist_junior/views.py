from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Categories, Post

# a page listing all the categories
class CategoriesListView(ListView):
    model = Categories
    template_name = "craigslist_junior/categories_list.html"
    context_object_name = "categories"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["title"] = "Categories"
        return context

# a page with a form to create a new category
class CategoriesNewView(CreateView):
    model = Categories
    template_name = "craigslist_junior/categories_create.html"
    fields = ('name',)

    def get_success_url(self):
        return reverse_lazy("cat_list")

# a page to view the detail of a specific category and a list of all of its associated posts
class CategoriesDetailView(ListView):
    model = Post
    template_name = "craigslist_junior/categories_detail.html"
    context_object_name = "posts"
    pk_url_kwarg = "category_id"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        title = Categories.objects.get(pk=self.kwargs["category_id"])
        context["title"] = title.name
        context["category_id"] = self.kwargs["category_id"]
        return context

    def get_queryset(self):
        category_id = self.kwargs["category_id"]
        return Post.objects.filter(categories__id = category_id)

# A page with a form to update a specific category, with current values filled in already. Also include the ability to delete the specific category here.
class CategoriesEditView(UpdateView):
    model = Categories
    template_name = "craigslist_junior/categories_edit.html"
    fields = ('name', )
    context_object_name = "cat"
    pk_url_kwarg = "category_id"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy("cat_list")


# A page with a form to delete a specific category.
class CategoriesDeleteView(DeleteView):
    model = Categories
    template_name = "craigslist_junior/categories_delete.html"
    context_object_name = "cat"
    pk_url_kwarg = "category_id"

    def get_success_url(self):
        return reverse_lazy("cat_list")

# A page with a form to create a new post, under the current category by default
class PostsNewView(CreateView):
    model = Post
    template_name = "craigslist_junior/post_create.html"
    fields = ('title','description')

    def form_valid(self, form):
        form = form.save(commit=False)
        form.categories = Categories.objects.get(pk=self.kwargs['category_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("cat_detail", kwargs={"category_id": self.kwargs["category_id"]})

# a page to view the detail of a specific post. Also include the ability to go back to the parent category detail page
class PostDetailView(DetailView):
    model = Post
    template_name = "craigslist_junior/post_detail.html"
    context_object_name = "post"
    pk_url_kwarg = "post_id"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

# A page with a form to update a specific post, with current values filled in already. Also include the ability to delete the specific post here
class PostEditView(UpdateView):
    model = Post
    template_name = "craigslist_junior/post_edit.html"
    fields = ('title', 'description')
    pk_url_kwarg = "post_id"

    def get_success_url(self):
        return reverse_lazy("cat_detail", kwargs={"category_id": self.kwargs["category_id"]})

# A page with a form to delete a specific post
class PostDeleteView(DeleteView):
    model = Post
    template_name = "craigslist_junior/post_delete.html"
    context_object_name = "post"
    pk_url_kwarg = "post_id"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        title = Categories.objects.get(pk=self.kwargs["category_id"])
        context["title"] = title.name
        return context

    def get_success_url(self):
        return reverse_lazy("cat_detail", kwargs={"category_id": self.kwargs["category_id"]})



