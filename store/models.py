from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
