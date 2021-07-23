from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.name

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=175)
    posted_by = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"