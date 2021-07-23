from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Categorie'

    def __str__(self):
        return f'{self.name}'

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title}'