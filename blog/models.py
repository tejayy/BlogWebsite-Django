from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime


# Create your models here.
'''POST MODEL'''
class Post(models.Model):
    title = models.CharField(max_length=100)
    title_tag = models.CharField(max_length=100, default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.title}  {self.author}'
    
    def get_absolute_url(self):
        return reverse('home')