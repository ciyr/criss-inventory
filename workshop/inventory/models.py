import datetime
from enum import unique
from django.db import models
import json
from django.urls import reverse

from workshop import settings

# Create your models here.

class Inventory(models.Model):
    itemId = models.IntegerField(unique=True)
    itemName = models.CharField(max_length=1000)
    quantity = models.IntegerField()


class Transaction(models.Model):
    itemName = models.CharField(max_length=1000)
    itemId = models.ForeignKey(Inventory,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateField()
    time = models.TimeField(default='00:00')
    issuee = models.CharField(max_length=1000)
    approved = models.BooleanField(default=False)
