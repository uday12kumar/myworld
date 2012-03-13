"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client


class SimpleTest(TestCase):
    def test_user_authentication(self):
        client_check = Client()
        response = client_check.post('/user_authentication' ,{'username': 'uday', 'password': 'hello'})
        self.assertEqual(response.status_code, 200)
