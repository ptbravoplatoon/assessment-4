from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255,default="")
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    #author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    content = models.TextField()
    short_description = models.TextField(default="")
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.CharField(max_length=255,default="")
    created_on = models.DateTimeField(auto_now_add=True)    

