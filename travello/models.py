from django.db import models

# Create your models here.

#class destination:  
  
    #name:str    to execute this comment below
    #img:str
    #desc:str
    #price:float
    #offer:bool


 # we are going to convert this class into a model or a table
class destination(models.Model):  # we are going to convert this class into a model or a table
  
    name= models.CharField(max_length= 100)    # https://docs.djangoproject.com/en/3.0/topics/db/models/
    img= models.ImageField(upload_to='pics') # we put image in the folder
    desc= models.TextField()
    price= models.IntegerField()
    offer= models.BooleanField(False)# python manage.py createsuper , this creates a superuser