# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Cookie

# Create your tests here.
class CookieTests(TestCase):
    
    def test_str(self):
        test_name = Cookie(name='A Cookie')
        self. assertEqual(str(test_name), 'A Cookie')