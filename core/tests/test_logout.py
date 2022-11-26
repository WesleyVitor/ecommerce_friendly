from django.test import TestCase, Client
from django.urls import reverse

from django.contrib.auth.models import User
from django.core.cache import cache

EMAIL_USER="wesley@gmail.com"
USERNAME_USER = "wesleyvitor"
PASSWORD_USER = "123456aa"

        

class LogoutTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.cliente = Client()
        self.user:User = User.objects.create_user(email=EMAIL_USER,username=USERNAME_USER,password=PASSWORD_USER)
        self.user.is_staff = True
        self.user.save()
        
    def test_logout_after_authenticate(self):
        url_login = reverse('login')
        url_logout = reverse('logout')
        self.cliente.post(url_login, {"username":USERNAME_USER, "password":PASSWORD_USER})
        response = self.cliente.get(url_logout)
        
        self.assertEqual(response.wsgi_request.user.is_authenticated, False)
    def test_logout_before_authenticate(self):
        
        url_logout = reverse('logout')
        
        response = self.cliente.get(url_logout)
        self.assertEqual(response.status_code, 403)