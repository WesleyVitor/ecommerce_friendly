from django.test import TestCase, Client
from django.urls import reverse

from django.contrib.auth.models import User
from core.models import Product


EMAIL_USER="wesley@gmail.com"
USERNAME_USER = "wesleyvitor"
PASSWORD_USER = "123456aa"
EMAIL_USER_WITHOUT_PERMISSION="wesley2@gmail.com"
USERNAME_USER_WITHOUT_PERMISSION = "wesleyvitor2"
PASSWORD_USER_WITHOUT_PERMISSION = "123456aa"

class ProductTest(TestCase):
    @classmethod
    def setUpTestData(self):
        
        self.user:User = User.objects.create_user(email=EMAIL_USER,username=USERNAME_USER,
        password=PASSWORD_USER,is_staff=True)
        self.user.save()
        self.user_without_permission:User = User.objects.create_user(email=EMAIL_USER_WITHOUT_PERMISSION,
        username=USERNAME_USER_WITHOUT_PERMISSION,
        password=PASSWORD_USER_WITHOUT_PERMISSION,
        is_staff=False)
        self.user_without_permission.save()
    
    
    def test_product_list_after_authenticate(self):
        
        cliente = Client()
        cliente.login(username=USERNAME_USER,password=PASSWORD_USER)
        
        url = reverse('product')
        response = cliente.get(url)
        
        self.assertEqual(response.status_code, 200)
    def test_product_created_after_authenticate(self):
        
        cliente = Client()
        cliente.login(username=USERNAME_USER,password=PASSWORD_USER)
        
        url = reverse('product')
        response = cliente.post(url, {"name":"arroz", "description":"muito bom", "price":"20"})
        product = Product.objects.get(id=1)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(product.name,'arroz')
        self.assertEqual(product.description,'muito bom')
        self.assertEqual(product.price,20)
    def test_product_created_without_permission(self):
        
        cliente = Client()
        cliente.login(username=USERNAME_USER_WITHOUT_PERMISSION,password=PASSWORD_USER_WITHOUT_PERMISSION)
        url = reverse('product')
        response = cliente.post(url, {"name":"arroz", "description":"muito bom", "price":"20"})
        
        self.assertEqual(response.status_code, 403)
        