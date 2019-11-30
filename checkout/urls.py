from django.conf.urls import url
from .views import checkout, ordersent

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    url(r'^ordersent/', ordersent, name='ordersent'),
]