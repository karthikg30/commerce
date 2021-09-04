from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class customer(models.Model):
    User = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
    cust_id = models.CharField(max_length=50, primary_key = True)
    cust_name  = models.CharField(max_length=50, null = True)
    phone = models.CharField(max_length=30, null = True)
    email = models.CharField(max_length=40, null = True)
    profile_pic = models.ImageField(null = True, blank = True)
    date_created = models.DateField(auto_created = True, null = True)
    c_user = models.CharField(max_length=50, null = True)
    date_modified = models.DateField(null = True, blank = True)
    m_user = models.CharField(max_length=100, null = True, blank = True)

    def __str__(self):
        return self.cust_name

class tags(models.Model):
    Tag_name = models.CharField(max_length=50, null = True)
    date_created = models.DateField(auto_created = True, null = True)
    c_user = models.CharField(max_length=50, null = True)
    date_modified = models.DateField(null = True, blank = True)
    m_user = models.CharField(max_length=100, null = True, blank = True)
    

    def __str__(self):
        return self.Tag_name


class  products(models.Model):

    category = (
        ('IN', 'Indoor'),
        ('OUT', 'Outdoor'),
    )

    name = models.CharField(max_length = 500, null = True)
    price = models.FloatField(null = True)
    category = models.CharField(max_length = 200, null = True, choices=category)
    description = models.CharField(max_length = 300, null = True)
    date_created = models.DateField(auto_created=True, null = True)
    date_modified = models.DateField(null = True, blank = True)
    m_user = models.CharField(max_length=100, null = True, blank = True)
    tags = models.ManyToManyField(tags)

    def __str__(self):
        return self.name


class order(models.Model):

    status = (
        ('Pending', 'Pending'), 
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
    )

    customer = models.ForeignKey(customer, null = True, to_field= "cust_id", on_delete = models.SET_NULL)
    product = models.ForeignKey(products, null = True, on_delete = models.SET_NULL)
    date_created = models.DateField(auto_created= True)
    status = models.CharField(max_length=50, null = True, choices = status)
    date_modified = models.DateField(null = True, blank = True)
    m_user = models.CharField(max_length=100, null = True, blank = True)

    def __str__(self):
        return (self.product.name + '-' + self.customer.cust_name)