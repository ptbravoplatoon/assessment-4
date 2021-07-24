from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    def __str__(self):
        return self.category_name


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='posts')

    def __str__(self):
        return f"{self.title}, price={self.price}"