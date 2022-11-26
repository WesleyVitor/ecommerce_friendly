from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework import status
from django.core.exceptions import PermissionDenied
from core.models import Product
from core.serializer import OutputProductSerializer, InputProductSerializer
from core.permissions import IsAdminUser
class LoginAPIView(APIView):

    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        if username and password:
            user = authenticate(request=request, username=username, password=password)
            if not user:
                raise PermissionDenied
        else:
            raise PermissionDenied
        
        login(request=request, user=user)
        
        return Response(data=None, status=status.HTTP_200_OK)

class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    
    def get(self, request):
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


