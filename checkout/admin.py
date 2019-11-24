# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import MakeOrder, OrderLineItem

# Register your models here.


class OrderLineAdminInLine(admin.TabularInline):
    model = OrderLineItem

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInLine, )
    
admin.site.register(MakeOrder, OrderAdmin)