from django.shortcuts import get_object_or_404, render, redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import stripe

stripe.api_key = settings.STRIPE_SECRET

def makedonationkey(request):
    key = settings.STRIPE_PUBLISHABLE

    context = {
        'key': key
    }

    return render(request, 'donate.html', context)

def donation_submit(request):
    """A view that charges the user through the use of STRIPE"""
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount = 1000,
            currency = 'EUR',
            description = 'Cookie Shop Donation',
            source = request.POST['stripeToken']
        )
        messages.success(request, 'Thank you for your donation!')
        return redirect('index')