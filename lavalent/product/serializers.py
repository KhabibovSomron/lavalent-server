from rest_framework import serializers
from .models import Brand, Category, Product, ProductImage, ProductSize


class CategorySerializer(serializers.ModelSerializer):
    """Список категории"""
    class Meta:
        model = Category
        fields = ('id', 'title', 'url', 'image')


class BrandSerializer(serializers.ModelSerializer):
    """Список брендов"""
    class Meta:
        model = Brand
        fields = ('id', 'title', 'url', 'image')


class ShortBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'title')

class ProductSerializer(serializers.ModelSerializer):
    """Список товаров"""
    brand = ShortBrandSerializer(read_only=True)
    class Meta:
        model = Product
        fields = ('id', 'vendor_code', 'price', 'material', 'poster', 'category', 'brand')


class ProductDetailSerializer(serializers.ModelSerializer):
    """Детальное описание товара"""
    brand = serializers.SlugRelatedField(slug_field="title", read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'vendor_code', 'price', 'material', 'brand', 'description', 'characteristic')


class ProductImageSerializer(serializers.ModelSerializer):
    """Список Изображения товара"""

    class Meta:
        model = ProductImage
        exclude = ('product',)


class ProductSizesSerializer(serializers.ModelSerializer):
    """Список размеров товара"""

    class Meta:
        model = ProductSize
        exclude = ('product',)

    