from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Category, Brand, KeyWord, Product, ProductImage, ProductSize

admin.site.site_header = "Lavalent Administration"
admin.site.unregister(Group)

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
    search_fields = ("product__vendor_code", )

@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ("id", "size")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "vendor_code", "material", "category", "brand", "price")
    list_filter = ( "brand", "category")
    search_fields = ("vendor_code", )