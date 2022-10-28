from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'Name', 'Desc', 'Type', 'Quantity',
                  'Price', 'Provider_id', 'Product_pic', 'Active')



