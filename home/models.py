from django.db import models


# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    a_email = models.CharField(max_length=50)
    principal_name = models.CharField(max_length=100)
    principal_email = models.EmailField(max_length=50)
    password = models.CharField(max_length=256)
    code = models.CharField(max_length=10, unique=True)

class Book (models.Model):
    class_name = models.CharField(max_length=50)
    bundle = models.BooleanField
    perticular = models.CharField(max_length=50)
    ammount = models.IntegerField
    tax = models.IntegerField
    total = models.IntegerField

