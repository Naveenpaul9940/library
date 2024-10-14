from django.db import models
from django.template.defaultfilters import yesno
from django.contrib.auth.models import User


class Reader(models.Model):
    reader_id = models.CharField(max_length=200, unique=True, default='default_reader_id')
    name = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=200)
    address = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    image = models.ImageField(upload_to='products/')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name



def __str__(self):
    return self.name
