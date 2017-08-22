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
    school_name = models.ForeignKey(School)
    class_name = models.CharField(max_length=50)
    bundle = models.CharField(max_length=20)
    particulars = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=7,decimal_places=3,default=0)
    tax_CGST = models.DecimalField(max_digits=7,decimal_places=3,default=0)
    tax_SGST = models.DecimalField(max_digits=7,decimal_places=3,default=0)
    total = models.DecimalField(max_digits=7,decimal_places=3,default=0)

