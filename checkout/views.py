# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import Payment, MakeOrder
from .models import OrderLineItem
from django.utils import timezone
from cookie.models import Cookie
from django.conf import settings
import stripe


# Create your views here.

stripe.api_key = settings.STRIPE_SECRET

def ordersent(request):
    """A view that will render ordersent.html"""
    return render(request, "ordersent.html")


@login_required()
def checkout(request):
    """If the request is post and forms are valid, then it will render the forms allowing users to submit their payment"""
    if request.method=="POST":
        order_form = MakeOrder(request.POST)
        payment_form = Payment(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            makeorder = order_form.save(commit=False)
            makeorder.date = timezone.now()
            makeorder.save()
            
            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Cookie, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    makeorder = makeorder, 
                    cookie = product, 
                    quantity = quantity
                    )
                order_line_item.save()
                
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "EUR",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
                
            if customer.paid:
                request.session['cart'] = {}
                return redirect(reverse('ordersent'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = Payment()
        order_form = MakeOrder()
        
    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
                