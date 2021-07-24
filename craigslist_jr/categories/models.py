from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey

class Category(models.Model):
    title = CharField(max_length=50)
    description = CharField(max_length=1000)

class Post(models.Model):
    category = ForeignKey(Category, on_delete=models.CASCADE)
    title = CharField(max_length=50)
    description = CharField(max_length=1000)