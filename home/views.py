# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse, HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, "index.html")
    
def about(request):
    return render(request, "about.html")