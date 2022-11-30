from django.test import TestCase, client
from core.models import Product, ShoppingCart, ItemProduct, Buy
from django.contrib.auth.models import User
from django.urls import reverse
EMAIL_USER="wesley@gmail.com"
USERNAME_USER = "wesleyvitor"
PASSWORD_USER = "123456aa"
EMAIL_USER_WITHOUT_PERMISSION="wesley2@gmail.com"
USERNAME_USER_WITHOUT_PERMISSION = "wesleyvitor2"
PASSWORD_USER_WITHOUT_PERMISSION = "123456aa"
class ShoppingCartTest(TestCase):
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
    def test_route_Buy_view(self):
        cliente = client.Client()
        cliente.login(username=USERNAME_USER, password=PASSWORD_USER)

        p1 = Product.objects.create(name='Arroz', description="Muito Bom", price=20)
        url = reverse("shoppingcart")
        data = {
            "product":p1.pk,
            "amount":30 
        }
        response = cliente.post(url,data)
        self.assertEqual(response.status_code, 201)
    
    def test_creating_a_shoppingcart(self):
        cliente = client.Client()
        cliente.login(username=USERNAME_USER, password=PASSWORD_USER)

        p1 = Product.objects.create(name='Arroz', description="Muito Bom", price=20)
        

        data = {
            "product":p1.pk,
            "amount":30 
        }
        url = reverse("shoppingcart")
        response = cliente.post(url, data)
        

        self.assertEqual(ItemProduct.objects.count(), 1)
        self.assertEqual(ShoppingCart.objects.count(), 1)

    def test_without_pass_payload(self):
        cliente = client.Client()
        cliente.login(username=USERNAME_USER, password=PASSWORD_USER)

        
        url = reverse("shoppingcart")
        response = cliente.post(url)
        self.assertEqual(response.status_code, 406)
        
    def test_product_not_exist(self):
        cliente = client.Client()
        cliente.login(username=USERNAME_USER, password=PASSWORD_USER)

        data = {
            "product":1,
            "amount":30 
        }
        
        url = reverse("shoppingcart")
        response = cliente.post(url,data)
        self.assertEqual(response.status_code, 400)

    def test_add_two_product_to_some_shoppingcart(self):
        cliente = client.Client()
        cliente.login(username=USERNAME_USER, password=PASSWORD_USER)

        p1 = Product.objects.create(name='Arroz', description="Muito Bom", price=20)
        data = {
            "product":p1.pk,
            "amount":30 
        }
        url = reverse("shoppingcart")
        cliente.post(url, data)
        
        p2 = Product.objects.create(name='Batata', description="Muito Bom", price=10)
        data = {
            "product":p2.pk,
            "amount":30 
        }
        url = reverse("shoppingcart")
        cliente.post(url, data)
        
        list_items = ShoppingCart.objects.get(id=1).list_items.all()
        a=1
        self.assertEqual(list_items.count(), 2)
        
