from cookie.models import Cookie


def cart_items(request):

    items_in_cart = []
    
    return {'items_in_cart': items_in_cart}