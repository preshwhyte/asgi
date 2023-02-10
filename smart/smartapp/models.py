from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class member(models.Model):
    Firstname=models.CharField(max_length=50)
    Lastname=models.CharField(max_length=50, )
    others=models.CharField(max_length=50, null=True)
    gender=models.CharField(max_length=10, null=True)
    email=models.EmailField(max_length=50)
    address=models.CharField(max_length=200)
    phone=models.IntegerField()
    profession=models.CharField(max_length=200, null=True)
    

    def __str__(self):
        return( f"{self.Firstname}" 
            f"{self.Lastname}"
        
        )

    # @property 
    # def imageURL(self):
    #     try:
    #         url=self.image.url

    #     except:
    #         url=''

    #     return url



class Comment(models.Model):
    name=models.CharField(max_length=45)
    post=models.CharField(max_length=500)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post, self.name)

class MemberList(models.Model):
    name=models.CharField(max_length=200)
    post=models.CharField(max_length=200)
    image=models.ImageField(upload_to='members/',null=True, blank=True)

class Item(models.Model):
    name = models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)





