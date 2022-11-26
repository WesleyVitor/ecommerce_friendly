from django.urls import path, include
from core.views import LoginAPIView, LogoutAPIView, ProductApiView
from rest_framework import routers

urlpatterns = [
    path('users/login/', LoginAPIView.as_view(), name='login'),
    path('users/logout/', LogoutAPIView.as_view(), name='logout'),
    path('users/product', ProductApiView.as_view(), name='product'),
]