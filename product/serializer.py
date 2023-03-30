from rest_framework import serializers
from .models import Product, Review, Category
from rest_framework.exceptions import ValidationError

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'name products_count'.split()



class ProductReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'title rating'.split()

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    price = serializers.IntegerField()
    category = serializers.IntegerField()

    def validate_category(self, category):
        try:
            Category.objects.get(id=category)
        except Category.DoesNotExist:
            raise ValidationError('Category not found!!!')
        return category


class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    products = serializers.ListField(child=serializers.CharField())
    stars = serializers.IntegerField()

    def validate_products(self, products):
        try:
            for i in products:
                Product.objects.get(product=i)
        except Product.DoesNotExist:
            raise ValidationError('Does not found')
        return products