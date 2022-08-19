from django.db import models

# Create your models here.
class GeeksModel(models.Model):
    fullname = models.CharField(max_length=200)
    phone= models.CharField(max_length=20)
    zipcode=models.CharField(max_length=20)
    address = models.TextField(max_length=200)



