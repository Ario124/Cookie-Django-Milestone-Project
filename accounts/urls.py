from django.conf.urls import url, include
from accounts.views import login, registration, logout


urlpatterns = [
    url(r'^login/', login, name="login"),
    url(r'^register/',  registration, name="register"),
    url(r'^logout/', logout, name="logout"),
]