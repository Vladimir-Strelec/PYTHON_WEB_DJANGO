from rest_framework import serializers

from shop_jwt_auth.product.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
