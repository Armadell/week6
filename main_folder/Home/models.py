
import email
from pydoc import describe
from django.db import models

# Create your models here.

class book(models.Model):
    name=models.CharField(max_length=200)
    picture=models.ImageField(blank=True)
    author=models.CharField(max_length=50,default='anonymous')
    email=models.EmailField(blank=True)
    describe=models.TextField()
    def __str__(self):
        return self.name
