from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from core.serializer import UserSerializer
from rest_framework import status
from django.core.exceptions import PermissionDenied
from rest_framework.authentication import BasicAuthentication
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




# Create your views here.
