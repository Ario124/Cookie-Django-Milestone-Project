# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from cookie.models import Cookie

# Create your models here.

class MakeOrder(models.Model):
    """A model that will let the user input personal information to be used as delivery"""
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address = models.CharField(max_length=40, blank=False)
    date = models.DateField()
    
    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name) 
        
class OrderLineItem(models.Model):
    makeorder = models.ForeignKey(MakeOrder, null=False, on_delete=models.CASCADE)
    cookie = models.ForeignKey(Cookie, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)
    
    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.cookie, self.cookie.price)