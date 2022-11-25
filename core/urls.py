from django.urls import path
from core.views import LoginAPIView


urlpatterns = [
    path('users/login/', LoginAPIView.as_view(), name='login'),
]