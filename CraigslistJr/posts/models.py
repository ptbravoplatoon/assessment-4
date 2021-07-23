from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f"Cat: {self.category.name}, Title: {self.title}"