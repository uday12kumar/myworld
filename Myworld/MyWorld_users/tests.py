"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from Myworld.MyWorld_users.models import UserProfiles


class SimpleTest(TestCase):
    def test_user_authentication(self):
        client_check = Client()
        response = client_check.post('/user_authentication/' ,{'username': 'admin', 'password': 'admin'})
        self.assertEqual(response.status_code, 200)

    def test_add_user(self):
        client_regester = Client()
        user_count = UserProfiles.objects.all().count()
        response = client_regester.post('/user_authentication/' ,{'username': 'admin', 'password': 'admin'})
        self.assertEqual(response.status_code, 200)
    
    def test_send_mail(self):
        
        
        