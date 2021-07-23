from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    item_name = models.CharField(max_length=100)
    item_desc = models.TextField()

    def __str__(self):
        return self.item_name
