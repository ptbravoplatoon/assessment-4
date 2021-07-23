from django.db import models
from django.db.models.deletion import CASCADE

class Categories(models.Model):
    name = models.CharField(max_length=100)
    createdOn = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}, {self.createdOn}"

class Post(models.Model):
    categories = models.ForeignKey(Categories, on_delete=CASCADE, related_name="posts")
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.title}, {self.categories.name}"