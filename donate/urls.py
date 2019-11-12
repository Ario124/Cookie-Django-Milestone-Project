from django.conf.urls import url, include
from donate.views import donate

urlpatterns = [
    url(r'^donate/', donate, name="donate"),
]