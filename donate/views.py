# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse, HttpResponseRedirect


# Create your views here.

def donate(request):
    return render(request, "donate.html")