from django.shortcuts import render
from django.http import HttpResponse
from .models import Category,Brand,Product
from rest_framework import viewsets
from .serializers import CategorySerializers,BrandSerializers,ProductSerializers
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema 

# Create your views here.
class CategoryViewSet(viewsets.ViewSet):
    queryset=Category.objects.all()
    
    @extend_schema(responses=CategorySerializers)
    def list(self, request):
        print(f"Request received: {request}")  # Example usage of the request parameter
        serializer = CategorySerializers(self.queryset, many=True)
        return Response(serializer.data)


class BrandViewSet(viewsets.ViewSet):
    queryset=Brand.objects.all()
    
    @extend_schema(responses=BrandSerializers)
    def list(self, request):
        print(f"Request received: {request}")  # Example usage of the request parameter
        serializer = BrandSerializers(self.queryset, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):
        
    queryset=Product.objects.all()
    
    @extend_schema(responses=ProductSerializers)
    def list(self, request):
        print(f"Request received: {request}")  # Example usage of the request parameter
        serializer = ProductSerializers(self.queryset, many=True)
        return Response(serializer.data)