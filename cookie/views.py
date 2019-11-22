# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from .models import Cookie
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def allcookies(request):
    cookies = Cookie.objects.all()
    return render(request, "cookie.html", {"cookies": cookies})
