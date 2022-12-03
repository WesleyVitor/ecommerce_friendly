from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework import status
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from rest_framework.authtoken.models import Token
from core.models import Product, ItemProduct,ShoppingCart, Buy
from core.serializer import (
    OutputProductSerializer, InputProductSerializer, InputShoppingCartSerializer)
from core.permissions import IsAdminUser
class LoginAPIView(APIView):

    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        if username and password:
            user = authenticate(request=request, username=username, password=password)
            if not user:
                print(username)
                raise PermissionDenied
        else:
            print(username)
            raise PermissionDenied
        
        login(request=request, user=user)
        token, created = Token.objects.get_or_create(user=user)
        return Response(data={'token':token.key}, status=status.HTTP_200_OK)

class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    
    def get(self, request):
        token = Token.objects.get(user=request.user)
        token.delete()
        logout(request)
        return Response(status=status.HTTP_200_OK)

class ProductApiView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]
    def get(self, request):
        
        products = Product.objects.all()
        serializer = OutputProductSerializer(products, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer:InputProductSerializer = InputProductSerializer(data={
            'name':request.data['name'],
            'description':request.data['description'],
            'price':request.data['price']
        })
        serializer.is_valid(raise_exception=True)
        product = Product.objects.create(name=serializer['name'].value,
        description=serializer['description'].value, 
        price=float(serializer['price'].value))
        product.save()
        return Response(data=None, status=status.HTTP_201_CREATED)

class ShoppingCartApiView(APIView):
    authentication_classes = [SessionAuthentication]
    def post(self, request:Request):
        keys = request.data.keys()
        if ('product' and 'amount') not in keys:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        
        data = {
            'product':request.data['product'],
            'amount':int(request.data['amount'])    
        }
        serializer = InputShoppingCartSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        
        try:
            p1 = Product.objects.get(pk=serializer['product'].value)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        amount = serializer['amount'].value

        item = ItemProduct.objects.create(product=p1, amount=amount)
        user = request.user

        try:
            shoppingCart = user.shoppingcart
        except ObjectDoesNotExist:
            shoppingCart = ShoppingCart.objects.create(user=request.user) 
        
        
        shoppingCart.list_items.add(item)
        return Response(status=status.HTTP_201_CREATED)
        
class BuyApiView(APIView):
    authentication_classes = [SessionAuthentication]

    def get(self, request):
        try:
            buys = Buy.objects.filter(user=request.user)
            
            shoppingcarts = []
            for buy in buys:
                shoppingCart = buy.shoppingcart
                items = []

                for item in shoppingCart.list_items.all():
                    obj_item = {
                        'product':item.product.name, 'amount':item.amount}
                    items.append(obj_item)
                obj = {
                    'id':shoppingCart.pk,
                    'items':items
                }
                shoppingcarts.append(obj)
            data = {
                'shoppingcart':shoppingcarts
            }
            return Response(data=data, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request:Request):
        user=  request.user
        try:
            shoppingCart:ShoppingCart = user.shoppingcart
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            b1 = Buy.objects.create(shoppingcart=shoppingCart, user=user)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(status=status.HTTP_201_CREATED)        
