from django.test import TestCase, Client
from django.urls import reverse

from django.contrib.auth.models import User



EMAIL_USER="wesley@gmail.com"
USERNAME_USER = "wesleyvitor"
PASSWORD_USER = "123456aa"

class ProductTest(TestCase):
    @classmethod
    def setUpTestData(self):
        
        self.user:User = User.objects.create_user(email=EMAIL_USER,username=USERNAME_USER,password=PASSWORD_USER,is_staff=True)
        self.user.save()
    
    
    def test_product_list_after_authenticate(self):
        
        cliente = Client()
        cliente.login(username=USERNAME_USER,password=PASSWORD_USER)
        
        url = reverse('product')
        response = cliente.get(url)
        
        self.assertEqual(response.status_code, 200)