from django.db import models
from django.utils import timezone 

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    list_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
