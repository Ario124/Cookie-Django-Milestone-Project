# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse, HttpResponseRedirect

# Create your views here.
def index(request):
    """A view that renders the index page"""
    return render(request, "index.html")
    
def about(request):
    """A view that renders the about page"""
    return render(request, "about.html")