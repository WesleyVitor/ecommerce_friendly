from django.urls import path
from core.views import LoginAPIView, LogoutAPIView


urlpatterns = [
    path('users/login/', LoginAPIView.as_view(), name='login'),
    path('users/logout/', LogoutAPIView.as_view(), name='logout'),
]