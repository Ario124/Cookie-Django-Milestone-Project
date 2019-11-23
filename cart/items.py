from django.shortcuts import get_object_or_404
from cookie.models import Cookie


def cart_items(request):

    cart = request.session.get('cart', {})

    items_in_cart = []
    total = 0
    product_count = 0
    
    for id, quantity in cart.items():
        cookie = get_object_or_404(Cookie, pk=id)
        total += quantity * cookie.price
        product_count += quantity
        items_in_cart.append({'id': id, 'quantity': quantity, 'cookie': cookie})
    
    return {'items_in_cart': items_in_cart, 'total': total, 'product_count': product_count}