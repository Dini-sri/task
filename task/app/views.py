from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from.models import products
from .serializers import productsserializer


class productsCurd(viewsets.ModelViewSet):
    queryset = products.objects.all()
    serializer_class = productsserializer
    #permission_classes = [permissions.AllowAny]