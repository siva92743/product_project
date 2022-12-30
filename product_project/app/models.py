from django.db import models

# Create your models here.


class Equipments(models.Model):
    product_name = models.CharField(max_length=25)
    category_id = models.IntegerField()
    price = models.IntegerField()


class Category(models.Model):
    name = models.CharField(max_length=25)


class Sales(models.Model):
    invoice_number = models.IntegerField()


class Customer(models.Model):
    name = models.CharField(max_length=25)
    dob = models.IntegerField()
    email = models.EmailField()