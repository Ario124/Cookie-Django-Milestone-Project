# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Cookie

# Create your tests here.
class CookieTests(TestCase):
    
    def test_str(self):
        self.assertEqual(len(Cookie.objects.all()), 0)
        new_cookie = Cookie(name='A Cookie', price = 30)
        new_cookie.save()
        self.assertEqual(len(Cookie.objects.all()), 1)