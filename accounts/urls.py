from django.conf.urls import url, include
from accounts.views import login, registration, logout
from accounts import url_reset


urlpatterns = [
    url(r'^login/', login, name="login"),
    url(r'^register/',  registration, name="register"),
    url(r'^logout/', logout, name="logout"),
    url(r'^password-reset/', include(url_reset))
]