from rest_framework import serializers
from .models import Brand,Category,Product


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = "__all__"
    

class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields = "__all__"
    

class ProductSerializers(serializers.ModelSerializer):
    brand=BrandSerializers()
    category=CategorySerializers()
    
    class Meta:
        model=Product
        fields = "__all__"
    