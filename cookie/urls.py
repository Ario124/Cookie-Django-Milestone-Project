from django.conf.urls import url, include
from .views import all_cookies


urlpatterns = [
    url(r'^$', all_cookies, name='allcookies'),
]