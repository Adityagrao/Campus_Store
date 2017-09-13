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

    def __str__(self):
        return self.name


class Book(models.Model):
    school_id = models.ForeignKey(School)
    name = models.CharField(max_length=100, default=None, blank=None)
    class_name = models.CharField(max_length=50)
    bundle = models.CharField(max_length=20)
    particulars = models.CharField(max_length=50)
    amount = models.FloatField()
    tax_CGST = models.FloatField()
    tax_SGST = models.FloatField()
    total = models.FloatField()

    def __str__(self):
        return self.name


class User(models.Model):
    school_id = models.ForeignKey(School)
    username = models.CharField(max_length=50, unique=True)
    dob = models.DateField()
    admission_number = models.CharField(max_length=50)
    name_of_parent = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=10)
    email_id = models.CharField(max_length=75)
    password = models.CharField(max_length=75)

    def __str__(self):
        return self.username


class Order(models.Model):
    user_id = models.ForeignKey(User)
    school_id = models.ForeignKey(School)
    book_id = models.ForeignKey(Book)
    order_time = models.DateTimeField(auto_now_add=True)
    total = models.FloatField()
    processed = models.BooleanField(default=False)

