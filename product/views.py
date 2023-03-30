from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Product, Review, Category
from .serializer import ProductSerializer, ReviewSerializer, CategorySerializer,\
    ProductReviewsSerializer
# Create your views here.

@api_view(['GET'])
def product_list_api_view(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        product = Product.objects.all()
        product.title = request.data.get('title')
        product.description = request.data.get('descripton')
        product.price = request.data.get('price')
        product.category = request.data.get('category')
        serializer = ProductSerializer(product)
        return Response(data=serializer.data)
    elif request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def product_review_api_view(request):
    product = Product.objects.all()
    serializer = ProductReviewsSerializer(product, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ReviewSerializer(review)
    return Response(data=serializer.data)


@api_view(['GET'])
def category_list_api_view(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CategorySerializer(category)
    return Response(data=serializer.data)


@api_view(['PUT'])
def create_product_api_view(request):
    product = Product.objects.all()
    product.title = request.data.get('title')
    product.description = request.data.get('descripton')
    product.price = request.data.get('price')
    product.category = request.data.get('category')
    return Response(data=ProductSerializer(product).data)