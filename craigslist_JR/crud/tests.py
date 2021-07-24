from django.test import TestCase, Client
from django.urls import reverse
from .models import Category, Post

#class for dummydata
class BasicTestEvents(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.e1 = Category.objects.create(category_name='Cars')

        cls.e2 = Category.objects.create(category_name='Boats')

        cls.e3 = Post.objects.create(category=cls.e1, title='chevy', description='old 100k miles',price = '1000')

        cls.e4 = Post.objects.create(category=cls.e2, title='Ford Boat', description='new boat',price = '7000')



# Test Category model
class TestEventModels(BasicTestEvents):
    
    def test_event_string_Category(self):
        self.assertIn("Cars",str(self.e1))

    def test_add_new_event_Category(self):
        all_events = Category.objects.all()
        self.assertEqual(all_events.count(),2)

        Category.objects.create(category_name='Baby Items')
        all_events = Category.objects.all()
        self.assertEqual(all_events.count(),3)

    def test_event_string_Post(self):
        self.assertIn("chevy",str(self.e3))


#Test view
class TestEventViews(BasicTestEvents):

    def setUp(self):
        self.client = Client()

    def test_all_returns_200(self):
        resp = self.client.get("/categories/")
        self.assertEqual(resp.status_code, 200)

    def test_all_returns_template(self):
        resp = self.client.get(reverse('new_category'))
        self.assertTemplateUsed(resp,'crud/category_form.html')

    def test_first_event_in_all(self):
        resp = self.client.get(reverse('all_categories'))
        self.assertContains(resp, "Cars", html=True)

    def test_post_request_redirects(self):
        body = {
            'category_name': 'motorcycles'
        }
        resp = self.client.post(reverse('new_category'), body)
        self.assertRedirects(resp,'/categories/3')
