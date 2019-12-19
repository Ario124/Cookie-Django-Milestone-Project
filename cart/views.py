# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def show_cart(request):
    """A view that renders and displays cart.html"""
    return render(request, "cart.html")

@login_required
def add_item_to_cart(request, id):
    """This view will add quantity of 1 to the cart that is loaded."""
    quantity = 1

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    if cart:
        messages.success(request, "Your item has been added to the cart.")
    return redirect(reverse('allcookies'))
    
@login_required
def edit_cart(request, id):
    """This view will request to get a quantity and if quantity is changed to 0 it will be deleted."""
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
        
    request.session['cart'] = cart
    return redirect(reverse(show_cart))
    
def remove_cookie(request, id):
    """A view that will request cart and delete if user loads the form by clicking"""
    cart = request.session.get('cart', {})
    
    cart.pop(str(id))
    request.session['cart'] = cart
    return redirect(reverse(show_cart))