
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogPost(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=100,null=True,blank=True)
    content = models.TextField(max_length=100, null=True, blank=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return str(self.user) # oe self.user.username



















# class User(AbstractUser):
#     is_shipper = models.BooleanField(default=False)
#     is_ftlsupp = models.BooleanField(default=False)
#     is_ptlsupp = models.BooleanField(default=False)
#     otp = models.IntegerField(default=1620122)
#     verified = models.BooleanField(default=False)



# class PhoneOTP(models.Model):
#      username = models.CharField(max_length=254, unique=True, blank=True, default=False)
#      phone_regex = RegexValidator( regex = r'^\+?1?\d{9,14}$', message = "Phone number must be entered in the form of +919999999999.")
#      name = models.CharField(max_length=254, blank=True, null=True)
#      phone = models.CharField(validators = [phone_regex], max_length=17)
#      otp = models.CharField(max_length=9, blank=True, null=True)
#      count = models.IntegerField(default=0, help_text = 'Number of opt_sent')
#      validated = models.BooleanField(default=False, help_text= 'if it is true, that means user have validate opt correctly in seconds')

#      def __str__(self):
#          return str(self.phone) + ' is sent ' + str(self.otp)






         
class Task(models.Model):
    title = models.CharField(max_length=200)
    completed= models.BooleanField(default=False, null=True, blank=True) 

    def __str__(self):
        return self.title 

class item(models.Model):
   
    name = models.CharField(max_length=38)
    done = models.BooleanField()
    def __str__(self):
        return self.name 


class stud(models.Model):

    skill = models.CharField(max_length=50)
    def __str__(self):
        return self.skill 

class man(models.Model):
     
    game = models.CharField(max_length=40)
    def __str__(self):
        return self.game 

class woman(models.Model): 
    cook = models.CharField(max_length=40)
    symbol = models.SlugField()
    price = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.cook 


class profile(models.Model):
    name = models.CharField(max_length=50)
    char = models.CharField(max_length=50)
    hobby =models.CharField(max_length=50)
    image = models.ImageField(null= True, upload_to = 'pics')
    def __str__(self):
        return self.name 

class upload(models.Model):
    image = models.ImageField(max_length=None, upload_to = 'pics')

class srikanth(models.Model):
    name = models.CharField(max_length=40)
    skill = models.CharField(max_length=30)
    def __str__(self):
        return self.skill 
        
