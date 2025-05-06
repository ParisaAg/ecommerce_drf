from django.shortcuts import render
from django.http import HttpResponse
from .models import Category
from rest_framework import viewsets
from .serializers import CategorySerializers
from rest_framework.response import Response

# Create your views here.

class CategoryViews(viewsets.ViewSet):
    queryset=Category.objects.all()
    
    def list(self,request):
        serializer = CategorySerializers(self.queryset, many=True)
        return Response(serializer.data)
