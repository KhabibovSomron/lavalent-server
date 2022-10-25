from django.contrib import admin
from .models import Category, Brand, KeyWord, Product, ProductImage, ProductSize

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "url", "image")


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "url", "image")


@admin.register(KeyWord)
class KeyWordAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("id", "image", 'product')

@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ("id", "size")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "vendor_code", "material", "category", "brand", "price")