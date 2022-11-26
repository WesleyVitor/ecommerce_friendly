from rest_framework import serializers
from core.models import Product


class InputProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=60)
    description = serializers.CharField(max_length=255)
    price = serializers.FloatField()
    


class OutputProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields=['id','name','description','price']
