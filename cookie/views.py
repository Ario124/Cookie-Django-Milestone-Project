# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from .models import Cookie

# Create your views here.
def allcookies(request):
    cookies = Cookie.objects.all()
    return render(request, "cookie.html", {"cookies": cookies})
