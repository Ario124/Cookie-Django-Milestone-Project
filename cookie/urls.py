from django.conf.urls import url, include
from .views import allcookies, cookie_details


urlpatterns = [
    url(r'^$', allcookies, name='allcookies'),
    url(r'^(?P<pk>\d+)/$', cookie_details, name='cookie_details'),
]