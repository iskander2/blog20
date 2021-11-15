
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    creat_at = models.DateTimeField(auto_now_add=True)
    author =models.CharField(max_length=150)
    image = models.ImageField(upload_to = 'images/')
    description = models.TextField()
    
    def __str__(self):
        return self.title