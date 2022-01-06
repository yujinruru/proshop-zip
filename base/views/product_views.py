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



@api_view(['POST'])
@permission_classes([IsAdminUser])
def createProduct(request):
    user = request.user

    product = Product.objects.create(
        user=user,
        name='Sample Name',
        price=0,
        brand='Sample Brand',
        countInStock=0,
        category='Sample Category',
        description=''
    )

    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)




@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateProduct(request, pk):
    data = request.data
    product = Product.objects.get(_id=pk)

    product.name = data['name']
    product.name = data['price']
    product.name = data['brand']
    product.name = data['countInStocke']
    product.name = data['category']
    product.description = data['description']


    product.save()

    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)
    



@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteProduct(requets, pk) :
    product = Product.objects.get(_id = pk)
    product.delete()
    return Response('producted deleted')