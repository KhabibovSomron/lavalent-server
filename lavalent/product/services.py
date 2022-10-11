from cgitb import lookup
from unicodedata import category
from django_filters import rest_framework as filters
from .models import Brand, Product

class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class BrandFilter(filters.FilterSet):
    category = CharFilterInFilter(lookup_expr='in')
    class Meta:
        model = Brand
        fields = ['category']

class ProductFilter(filters.FilterSet):
    category = filters.CharFilter(lookup_expr="in")
    brand = filters.CharFilter(lookup_expr="in")
    class Meta:
        model = Product
        fields = ['category', 'brand']