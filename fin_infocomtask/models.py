from turtle import title
from django.db import models

# Create your models here.
import io
from PIL import Image
import base64
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile


class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    age = models.PositiveIntegerField(null=True)
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
    photo= models.ImageField(upload_to='media',null=True, blank=True) 

    def __str__(self):
       
        return '%s %s %s' % (self.name, self.email,self.gender)

    def get_base64_encoded_image(photo):
        with open(photo, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')






        

# def decodeDesignImage(data):
#     try:
#         data = base64.b64decode(data.encode('UTF-8'))
#         buf = io.BytesIO(data)
#         img = Image.open(buf)
#         return img
#     except:
#         return None
#     finally:
#         img = decodeDesignImage(data)
#         img_io = io.BytesIO()
#         img.save(img_io, format='JPEG')
#         photo.image = InMemoryUploadedFile(img_io, field_name=None, name=token+".jpg", content_type='image/jpeg', size=img_io.tell, charset=None)
#         design.save()





 