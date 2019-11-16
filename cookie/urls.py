from django.conf.urls import url, include
from .views import allcookies


urlpatterns = [
    url(r'^$', allcookies, name='allcookies'),
]