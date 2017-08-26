from django.db import models


# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    alternate_email = models.CharField(max_length=50)
    principal_name = models.CharField(max_length=100)
    principal_email = models.EmailField(max_length=50)
    password = models.CharField(max_length=256)
    code = models.CharField(max_length=10, unique=True)
    status = models.BooleanField(default=True)


class Book(models.Model):
    School_name = models.CharField(max_length=50)
    class_name = models.CharField(max_length=50)
    bundle = models.CharField(max_length=20)
    particulars = models.CharField(max_length=50)
    amount = models.FloatField()
    tax_CGST = models.FloatField()
    tax_SGST = models.FloatField()
    total = models.FloatField()
