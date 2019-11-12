# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse, HttpResponseRedirect


# Create your views here.

def donate(request):
    """This is the view that will display the donate.html page"""
    return render(request, "donate.html")