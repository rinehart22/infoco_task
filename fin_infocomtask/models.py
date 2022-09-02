from turtle import title
from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    age = models.PositiveIntegerField()
    gender=models.CharField(max_length=20)
    phone_no=models.CharField(max_length=20)
    #address_details=models.
    h_no=models.CharField(max_length=200)
    street=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    #work_experience = dict
    company=models.CharField(max_length=200)
    from_date=models.DateField()
    to_date=models.DateField()
    address=models.CharField(max_length=200)
    #qualifications= dict
    qualification_name=models.CharField(max_length=200)
    percentage=models.FloatField()
    #projects=
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=200)
    #photo= base64 

    def __str__(self):
       
        return '%s %s %s' % (self.name, self.email,self.gender)