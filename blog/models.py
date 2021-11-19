

from django.db import models

# Create your models here.

class Category(models.Model):
    name =models.CharField(max_length=20,)

    def __str__(self):
        return self.name    

class Post(models.Model):
    title = models.CharField(max_length=150)
    creat_at = models.DateTimeField(auto_now_add=True)
    author =models.CharField(max_length=150)
    image = models.ImageField(upload_to = 'images/')
    category = models.ForeignKey(Category , on_delete=models.CASCADE,blank=True,null=True)
    short_description = models.TextField(max_length=200)
    description= models.TextField()
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    author =models.CharField(max_length=15)
    description =models.TextField(max_length=150)
    post =models.ForeignKey(Post,on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')  

    def __str__(self):
        return f'{self.author} -> {self.post}'     