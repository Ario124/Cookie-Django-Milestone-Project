from django.conf.urls import url
from .views import show_cart, add_item_to_cart, edit_cart, remove_cookie

urlpatterns = [
    url(r'^$', show_cart, name='show_cart'),
    url(r'^add/(?P<id>\d+)', add_item_to_cart, name='add_item_to_cart'),
    url(r'^edit/(?P<id>\d+)', edit_cart, name='edit_cart'),
    url(r'^remove/(?P<id>\d+)', remove_cookie, name='remove_cookie'),
]