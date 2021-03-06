"""cookieproject URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from home.views import index, about
from cookie.views import allcookies
from cookie import urls as urls_cookies
from checkout import urls as urls_checkout
from donate import urls as urls_donate
from .settings import MEDIA_ROOT
from django.views import static
from cart import urls as urls_cart

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^cookies/', include(urls_cookies)),
    url(r'^$', index, name='index'),
    url(r'^about/', about, name='about'),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^donate/', include(urls_donate)),
    url(r'^cart/', include(urls_cart)),
    url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),
    
]