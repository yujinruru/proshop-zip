from django.shortcuts import render
from django.contrib.auth.hashers import make_password


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status


from base.models import Product
from base.serializers import ProductSerializer



@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    sarializer = ProductSerializer(products, many=True)
    return Response(sarializer.data)


@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    sarializer = ProductSerializer(product, many=False)


    return Response(sarializer.data)