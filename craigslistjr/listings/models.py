from django.db import models

class Category(models.Model):
    topic = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/')
    description = models.TextField()
    phone_number = models.CharField(max_length=12)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}, {self.description[:20]}"