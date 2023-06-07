from django.db import models

# Table book

class book(models.Model):
    title=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    price=models.IntegerField()
    pdf=models.FileField(upload_to='book/pdf')
    cover=models.ImageField(upload_to='book/cover',null=True,blank=True)

class student(models.Model):
     f_name=models.CharField(max_length=20)
     l_name = models.CharField(max_length=20)
     age = models.IntegerField()
     place= models.CharField(max_length=20)
class factorial(models.Model):
    num=models.IntegerField()
class calculator(models.Model):
    n1=models.IntegerField()
    n2=models.IntegerField()
