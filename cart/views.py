# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# Create your views here.
def show_cart(request):
    return render(request, "cart.html")


def add_item_to_cart(request, id):
    quantity = 1

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    if cart:
        messages.success(request, "Your item has been added to the cart.")
    return redirect(reverse('allcookies'))
    
def edit_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    
    if quantity > 0:
        cart[id] = quantity
        
    request.session['cart'] = cart
    return redirect(reverse(show_cart))