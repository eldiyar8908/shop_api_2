from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Product, Review, Category
from .serializer import ProductSerializer, ReviewSerializer, CategorySerializer,\
    ProductReviewsSerializer, ProductValidateSerializer, CategoryValidateSerializer,\
    ReviewValidateSerializer
# Create your views here.


@api_view(['GET', 'POST'])
def product_list_api_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = ProductValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        price = serializer.validated_data.get('price')
        category_id = serializer.validated_data.get('category_id')
        product = Product.objects.create(title=title, description=description,
                                         price=price, category_id=category_id)
        return Response(data=ProductSerializer(product).data)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(data=serializer.data)

    elif request.method == 'PUT':
        serializer = ProductValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        product.title = serializer.validated_data.get('title')
        product.description = serializer.validated_data.get('description')
        product.price = serializer.validated_data.get('price')
        product.category = serializer.validated_data.get('category')
        product.save()
        return Response(data=ProductSerializer(product).data)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        text = request.data.get("text")
        stars = request.data.get("stars")
        product_id = request.data.get("product_id")
        review = Review.objects.create(text=text, stars=stars, product_id=product_id)
        return Response(data=ReviewSerializer(review).data)



@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductSerializer(review)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        review.text = request.data.get('text')
        review.stars = request.data.get('stars')
        review.product_id = request.data.get('product_id')
        review.save()
        return Response(data=ReviewSerializer(review).data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def product_review_api_view(request):
    product = Product.objects.all()
    serializer = ProductReviewsSerializer(product, many=True)
    return Response(data=serializer.data)




@api_view(['GET', 'POST'])
def category_list_api_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = CategoryValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        name = request.data.get('name')
        category = Category.objects.create(name=name)
        return Response(data=CategorySerializer(category).data)


@api_view(['GET'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        category.name = request.data.get('name')
        category.save()
        return Response(data=CategorySerializer(category).data)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def create_product_api_view(request):
    product = Product.objects.all()
    product.title = request.data.get('title')
    product.description = request.data.get('descripton')
    product.price = request.data.get('price')
    product.category = request.data.get('category')
    return Response(data=ProductSerializer(product).data)