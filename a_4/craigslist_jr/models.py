from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    item_name = models.CharField(max_length=100)
    item_desc = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="posts"
    )

    def __str__(self):
        return self.item_name
