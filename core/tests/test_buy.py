from django.test import TestCase, client
from django.contrib.auth.models import User
from django.urls import reverse
from core.models import ShoppingCart, Product, Buy
EMAIL_USER="wesley@gmail.com"
USERNAME_USER = "wesleyvitor"
PASSWORD_USER = "123456aa"
EMAIL_USER_WITHOUT_PERMISSION="wesley2@gmail.com"
USERNAME_USER_WITHOUT_PERMISSION = "wesleyvitor2"
PASSWORD_USER_WITHOUT_PERMISSION = "123456aa"
class BuyTest(TestCase):
    
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

    def test_route_buy_view(self):
        cliente = client.Client()
        cliente.login(username=USERNAME_USER, password=PASSWORD_USER)

        p1 = Product.objects.create(name='Arroz', description="Muito Bom", price=20)
        url = reverse("shoppingcart")
        data = {
            "product":p1.pk,
            "amount":30 
        }
        cliente.post(url,data)
        

        url = reverse("buy")
        
        response = cliente.post(url)
        self.assertEqual(response.status_code, 201)
    def test_do_a_buy(self):
        cliente = client.Client()
        cliente.login(username=USERNAME_USER, password=PASSWORD_USER)

        p1 = Product.objects.create(name='Arroz', description="Muito Bom", price=20)
        url = reverse("shoppingcart")
        data = {
            "product":p1.pk,
            "amount":30 
        }
        cliente.post(url,data)
        sc = ShoppingCart.objects.get(id=1)

        url = reverse("buy")
        
        response = cliente.post(url)
        self.assertEqual(Buy.objects.count(),1)
    def test_without_shoppingcart_to_buy(self):
        cliente = client.Client()
        cliente.login(username=USERNAME_USER, password=PASSWORD_USER)

        url = reverse("buy")
        
        response = cliente.post(url)
        self.assertEqual(response.status_code, 400)
    
   