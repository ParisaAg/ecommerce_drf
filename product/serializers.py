from rest_framework import serializers
from .models import Brand,Category,Product,ProductLine,ProductImage


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
    
class ProductImageSerializers(serializers.ModelSerializer):
    class Meta:
        model=ProductImage
        exclude=('id',)



class ProductLineSerializers(serializers.ModelSerializer):
    product_image=ProductImageSerializers(many=True)
    class Meta:
        model=ProductLine
        fields=( 'price','sku','stock_qty','order','product_image')
