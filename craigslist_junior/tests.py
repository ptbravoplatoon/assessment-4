from django.test import TestCase, Client
from .models import Categories, Post
from django.urls import reverse

class BasicTestSetup(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.s1 = Categories.objects.create(name="Land")
        cls.s2 = Categories.objects.create(name="Vehicles")
        cls.s3 = Post.objects.create(categories=cls.s1, title="Farm", description="20 Acres")
        cls.s4 = Post.objects.create(categories=cls.s1, title="House", description="3 Stories")
        cls.s5 = Post.objects.create(categories=cls.s1, title="Chevy Nova", description="1972")
        cls.s6 = Post.objects.create(categories=cls.s1, title="Ford Ranger", description="1991")

class TestModels(BasicTestSetup):

    def test_database(self):
        self.assertIn("Land", str(self.s1.name))
        self.assertIn("Vehicles", str(self.s2.name))
        self.assertIn("Land", str(self.s3.categories))
        self.assertIn("Farm", str(self.s3))
        all_posts = Post.objects.all()
        self.assertEqual(all_posts.count(), 4)
        all_cats = Categories.objects.all()
        self.assertEqual(all_cats.count(), 2)

class TestRosterViews(BasicTestSetup):

    def setUp(self):
        self.client = Client()

    def test_all_returns_200(self):
        resp = self.client.get("/categories/")
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get("/categories/" + str(self.s1.id) + "/")
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get("/categories/" + str(self.s2.id) + "/")
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get("/categories/" + str(self.s1.id) + "/posts/" + str(self.s3.id) + "/")
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get("/categories/" + str(self.s1.id) + "/posts/" + str(self.s4.id) + "/")
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get("/categories/" + str(self.s2.id) + "/posts/" + str(self.s5.id) + "/")
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get("/categories/" + str(self.s2.id) + "/posts/" + str(self.s6.id) + "/")
        self.assertEqual(resp.status_code, 200)

    def test_all_returns_template(self):
        # category templates
        resp = self.client.get(reverse("cat_list"))
        self.assertTemplateUsed(resp, 'craigslist_junior/categories_list.html')
        resp = self.client.get(reverse("cat_create"))
        self.assertTemplateUsed(resp, 'craigslist_junior/categories_create.html')
        resp = self.client.get(reverse("cat_detail", kwargs={"category_id": str(self.s2.id)}))
        self.assertTemplateUsed(resp, 'craigslist_junior/categories_detail.html')
        resp = self.client.get(reverse("cat_edit", kwargs={"category_id": str(self.s2.id)}))
        self.assertTemplateUsed(resp, 'craigslist_junior/categories_edit.html')
        resp = self.client.get(reverse("cat_delete", kwargs={"category_id": str(self.s2.id)}))
        self.assertTemplateUsed(resp, 'craigslist_junior/categories_delete.html')
        # post templates
        resp = self.client.get(reverse("post_detail", kwargs={"category_id": str(self.s1.id), "post_id": str(self.s3.id)}))
        self.assertTemplateUsed(resp, 'craigslist_junior/post_detail.html')
        resp = self.client.get(reverse("post_create", kwargs={"category_id": str(self.s1.id)}))
        self.assertTemplateUsed(resp, 'craigslist_junior/post_create.html')
        resp = self.client.get(reverse("post_edit", kwargs={"category_id": str(self.s1.id), "post_id": str(self.s3.id)}))
        self.assertTemplateUsed(resp, 'craigslist_junior/post_edit.html')
        resp = self.client.get(reverse("post_delete", kwargs={"category_id": str(self.s1.id), "post_id": str(self.s3.id)}))
        self.assertTemplateUsed(resp, 'craigslist_junior/post_delete.html')
