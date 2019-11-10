# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse, HttpResponseRedirect

# Create your views here.
def index(request):
    """This is the view that will display the index.html page"""
    return render(request, "index.html")
    
def about(request):
    """This is the view that will display the index.html page"""
    return render(request, "about.html")