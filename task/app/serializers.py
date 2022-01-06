from rest_framework .serializers import ModelSerializer
from .models import products

class productsserializer(ModelSerializer):
    class Meta:
        model=products
        fields=['Name','Cost_per_item','stock_quantity','volume']