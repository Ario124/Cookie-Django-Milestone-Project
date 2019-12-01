# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Cookie(models.Model):
    name = models.CharField(max_length=200, default='')
    info = models.TextField()
    detail = models.TextField(default='')
    amount = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    
    
    def __str__(self):
        return self.name