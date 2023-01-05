from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class member(models.Model):
    Firstname=models.CharField(max_length=50)
    Lastname=models.CharField(max_length=50)
    other=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    address=models.TextField()
    phone=models.IntegerField()

    def __str__(self):
        return self.Firstname


class Comment(models.Model):
    name=models.CharField(max_length=45)
    post=models.CharField(max_length=500)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post, self.name)


