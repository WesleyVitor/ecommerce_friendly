from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework import status
from django.core.exceptions import PermissionDenied
from core.models import Product
from core.serializer import OutputProductSerializer
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
        user=request.user.is_staff
        products = Product.objects.all()
        serializer = OutputProductSerializer(products, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


