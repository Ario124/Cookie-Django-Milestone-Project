from django.conf.urls import url
from .views import makedonationkey, donation_submit



urlpatterns = [
    url(r'^$', makedonationkey, name='makedonationkey'),
    url(r'^donation/', donation_submit, name='donation_submit'),
]