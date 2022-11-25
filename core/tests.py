from django.test import TestCase, Client
from django.urls import reverse
from core.models import CustomUser
from django.contrib.auth.models import User

class LoginTest(TestCase):
    @classmethod
    def setUpTestData(self):
        user = CustomUser.objects.create_user(email='wesley@gmail.com',username='wesleyvitor',password='123456aa', is_admin=False)
        user.save()
    def test_login(self):
        
        cliente = Client()
        url = reverse('login')
        response = cliente.post(url, {"username":"wesleyvitor", "password":"123456aa"})
        self.assertEqual(response.status_code,200)

# Create your tests here.
