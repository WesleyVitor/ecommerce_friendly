from django.urls import path, include
from core.views import LoginAPIView, LogoutAPIView, ProductApiView, ShoppingCartApiView,BuyApiView


urlpatterns = [
    path('users/login', LoginAPIView.as_view(), name='login'),
    path('users/logout', LogoutAPIView.as_view(), name='logout'),
    path('users/product', ProductApiView.as_view(), name='product'),
    path('shoppingcart/', ShoppingCartApiView.as_view(), name='shoppingcart'),
    path('buy/', BuyApiView.as_view(), name='buy'),
]