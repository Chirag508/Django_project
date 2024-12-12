from django.db import models

# Create your models here.
class customer_data(models.Model):
    cust_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.BigIntegerField()
    age = models.IntegerField()
    address = models.TextField()
    state = models.CharField(max_length=255)
    Registrationdate = models.DateTimeField(auto_now_add=True)
    updationdate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class news(models.Model):
    DateTime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    auther = models.CharField(max_length=255)
    body = models.TextField()
    def __str__(self):
        return self.title

class product(models.Model):
    name = models.CharField(max_length=255)
    details = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    Create_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name