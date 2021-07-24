from django.test import TestCase, Client
from .models import Category, Post
from django.urls import reverse, reverse_lazy


# Parent class to set up testing
class BaseListingsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.cat1 = Category.objects.create(name="Cat1", description="asdf")
        cls.cat2 = Category.objects.create(name="Cat2", description="qwer")
        cls.p1 = Post.objects.create(title="FirstPost", category=cls.cat1, posted_by="Alma",description="Post1 Description Text", price=11)
        cls.p2 = Post.objects.create(title="Second Post", category=cls.cat2, posted_by="Babbit",description="Post2 Description Text", price=22)
        cls.client = Client()



# Testing the Models: Category & Post
class TestListingsModels(BaseListingsTest):
    def test_category_attributes(self):
        first = Category.objects.get(pk=1)
        second = Category.objects.get(pk=2)
        self.assertEqual(self.cat1.name, first.name)
        self.assertEqual(self.cat2.description, second.description)
    def test_post_attributes(self):
        first = Post.objects.get(pk=1)
        second = Post.objects.get(pk=2)
        self.assertEqual(self.p1.title, first.title)
        self.assertEqual(self.p2.posted_by, second.posted_by)
    
    def test_add_new_category(self):
        all_cats = Category.objects.all()
        self.assertEqual(all_cats.count(), 2)
        Category.objects.create(name="Cat3")
        self.assertEqual(all_cats.count(), 3)
    
    def test_add_new_post(self):
        all_posts = Post.objects.all()
        self.assertEqual(all_posts.count(), 2)
        Post.objects.create(title="ThirdPost", category=self.cat2, posted_by="Clyde",description="Post3 Description Text", price=33)
        self.assertEqual(all_posts.count(), 3)

# Testing the Views::
# Category: Create
class TestCreateCategoriesView(BaseListingsTest):
    def test_list_categories_returns_200(self):
        response = self.client.get(reverse('new_category'))
        self.assertEqual(response.status_code, 200)
    def test_list_categories_returns_template(self):
        response = self.client.get(reverse('new_category'))
        self.assertTemplateUsed(response, "listings/new_category.html")
    def test_post_request_redirects(self):
        body = {
            "name": "Cat4",
            "description":"Category 4 description text"
        }
        resp = self.client.post(reverse("new_category"), body)
        self.assertRedirects(resp, reverse('list_categories'))
    def test_post_request_adds_cat(self):
        all_cats = Category.objects.all()
        body = {
            "name": "Cat4",
            "description":"Category 4 description text"
        }
        resp = self.client.post(reverse("new_category"), body)
        self.assertEqual(all_cats.count(), 3)
        



# Category: Read- List
class TestListCategories(BaseListingsTest):
    def test_list_categories_returns_200(self):
        response = self.client.get(reverse('list_categories'))
        self.assertEqual(response.status_code, 200)
    def test_list_categories_returns_template(self):
        response = self.client.get(reverse('list_categories'))
        self.assertTemplateUsed(response, "listings/list_categories.html")
    def test_first_category_in_list(self):
        response = self.client.get(reverse("list_categories"))
        self.assertContains(response, "Cat1:", html=True)
        self.assertContains(response, "asdf", html=True)



# Category: Read - Detail
class TestCategoryDetail(BaseListingsTest):
    def test_category_detail_returns_200(self):
        category_id = 1
        response = self.client.get(reverse('category_detail', kwargs={"category_id": category_id}))
        self.assertEqual(response.status_code, 200)
    def test_list_categories_returns_template(self):
        category_id = 1
        response = self.client.get(reverse('category_detail', kwargs={"category_id": category_id}))
        self.assertTemplateUsed(response, "listings/category_detail.html")
    def test_first_category_in_list(self):
        response = self.client.get(reverse("category_detail", kwargs = {"category_id":2}))
        self.assertContains(response, "Cat2 Posts:", html=True)
        self.assertContains(response, "qwer", html=True)


# Category: Update
class TestEditCategoryView(BaseListingsTest):
    # def test_edit_category_returns_200(self):
    #     response = self.client.get(reverse('edit_category', kwargs={"category_id":2}))
    #     self.assertEqual(response.status_code, 200)
    def test_edit_category_returns_template(self):
        response = self.client.get(reverse('edit_category', kwargs={"category_id":2}))
        self.assertTemplateUsed(response, "listings/edit_category.html")
    def test_post_request_redirects(self):
        body = {
            "name": "Cat2 Edit",
            "description":"EDITED Category 2 description text"
        }
        resp = self.client.post(reverse("edit_category", kwargs={"category_id":2}), body)
        self.assertRedirects(resp, reverse('category_detail', kwargs={"category_id":2}))
    def test_post_request_changes_cat(self):
        response = self.client.get(reverse("category_detail", kwargs = {"category_id":2}))
        self.assertContains(response, "Cat2 Posts:", html=True)
        self.client.post(reverse("edit_category", kwargs = {"category_id":2}), {"name": "Cat2edit", "description":"Category 4 description text"})
        response2 = self.client.get(reverse("category_detail", kwargs = {"category_id":2}))
        self.assertContains(response2, "Cat2edit Posts:", html=True)

# Category: Delete

class TestDeleteCategoriesView(BaseListingsTest):
    def test_delete_category(self):
        all_cats = Category.objects.all()
        self.assertEqual(all_cats.count(), 2)
        self.client.post(reverse("delete_category", kwargs = {"category_id":2}))
        self.assertEqual(all_cats.count(), 1)
# ---------------------- Post Views Tests -------------------
# Post: Create
class TestCreatePostsView(BaseListingsTest):
    def test_list_posts_returns_200(self):
        response = self.client.get(reverse('new_post', kwargs={"category_id":1}))
        self.assertEqual(response.status_code, 200)
    def test_list_post_returns_template(self):
        response = self.client.get(reverse('new_post', kwargs={"category_id":1}))
        self.assertTemplateUsed(response, "listings/new_post.html")
        
    def test_post_request_adds_post(self):
        all_posts = Post.objects.all()
        self.assertEqual(all_posts.count(), 2)
        body = {
            "title": "Post3",
            "posted_by": "Bess", 
            "description":"ljgkjkgfgh", 
            "price":33
            }
        self.client.post(reverse("new_post", kwargs={"category_id":1}), body)
        self.assertEqual(all_posts.count(), 3)


# Post: Read- List
class TestListPosts(BaseListingsTest):
    def test_list_categories_returns_template(self):
        response = self.client.get(reverse('category_detail', kwargs={"category_id":1}))
        self.assertTemplateUsed(response, "listings/category_detail.html")
    def test_first_post_in_list(self):
        response = self.client.get(reverse('category_detail', kwargs={"category_id":1}))
        self.assertContains(response, "FirstPost", html=True)

# Post: Read - Detail
class TestPostDetail(BaseListingsTest):
    def test_post_detail_returns_200(self):
        category_id = 1
        post_id=1
        response = self.client.get(reverse('post_detail', kwargs={"category_id": category_id, "post_id": post_id}))
        self.assertEqual(response.status_code, 200)
    def test_list_categories_returns_template(self):
        category_id = 1
        post_id=1
        response = self.client.get(reverse('post_detail', kwargs={"category_id": category_id, "post_id": post_id}))
        self.assertTemplateUsed(response, "listings/post_detail.html")

        
    # def test_post_detail_content(self):
    #     response = self.client.get(reverse('post_detail', kwargs={"category_id": 1, "post_id": 1}))
    #     self.assertContains(response, "All", html=True)
    #     self.assertContains(response, "Post1 Description Text", html=True)


# Post: Update
# Post: Delete