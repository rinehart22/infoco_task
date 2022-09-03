from turtle import title
from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    age = models.PositiveIntegerField()
    gender=models.CharField(max_length=20)
    phone_no=models.CharField(max_length=20)
    address_details=models.CharField(max_length=200)
    h_no=models.CharField(max_length=200)
    street=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    work_experience = models.CharField(max_length=200)
    company=models.CharField(max_length=200)
    from_date=models.DateField()
    to_date=models.DateField()
    address=models.CharField(max_length=200)
    qualifications = models.CharField(max_length=200)
    qualification_name=models.CharField(max_length=200)
    percentage=models.FloatField()
    projects = models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=200)
    photo= models.ImageField(upload_to='media') 

    def __str__(self):
       
        return '%s %s %s' % (self.name, self.email,self.gender)
