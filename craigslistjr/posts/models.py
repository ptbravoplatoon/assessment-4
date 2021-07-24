from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    date_created = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

class Post(models.Model):
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE, default=None, blank=True, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(default=None, blank=True, null=True)
    last_edit = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return f"{self.title} {self.date_created}"[:-10]
