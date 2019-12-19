# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse, HttpResponseRedirect, get_object_or_404
from .models import Cookie
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def allcookies(request):
    """A view that loads all the cookies and renders cookie.html"""
    cookies = Cookie.objects.all()
    return render(request, "cookie.html", {"cookies": cookies})


def cookie_details(request, pk):
    """A view that will load information about the selected item"""
    cookieinfo = get_object_or_404(Cookie, pk=pk)
    cookieinfo.save()
    return render(request, "cookie_details.html", {'cookieinfo': cookieinfo})