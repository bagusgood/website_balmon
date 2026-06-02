from django.db import models
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100, default="")
    body=models.TextField(default="")
    category = models.CharField(max_length=255, default="")
    image = models.ImageField(blank=True, default="logo.png")
    publish = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    slug = models.SlugField(blank=True, editable=False)
    
    def save(self):
        self.slug = slugify(self.title)
        super(Post, self).save()
    
    def __str__(self):
        return self.title

class Banner(models.Model):
    title= models.CharField(max_length=100)
    image = models.ImageField(blank=True, default="logo.png")
    
    def __str__(self):
        return self.title
    
    