from dataclasses import field
from rest_framework import serializers
from .models import Brand, Category, Product


class CategorySerializer(serializers.ModelSerializer):
    """Список категории"""
    class Meta:
        model = Category
        fields = ('id', 'title', 'url', 'image')


class BrandSerializer(serializers.ModelSerializer):
    """Список брендов"""
    class Meta:
        model = Brand
        fields = ('id', 'title', 'url')


class ProductSerializer(serializers.ModelSerializer):
    """Список товаров"""
    class Meta:
        model = Product
        fields = ('id', 'vendor_code', 'price', 'material', 'poster', 'category', 'brand')

class ProductDetailSerializer(serializers.ModelSerializer):
    """Детальное описание товара"""
    # my_brand = serializers.SerializerMethodField()
    # my_category = serializers.SerializerMethodField()

    class Meta:
        model = Product
        exclude = ('poster', )

    # def get_my_brand(self, obj):
    #     brand = Brand.objects.filter(id=obj.brand)
    #     serializer = BrandSerializer(brand)
    #     return (serializer.data)

    # def get_my_category(self, obj):
    #     category = Category.objects.filter(id=obj.category)
    #     serializer = CategorySerializer(category)
    #     return (serializer.data)
    