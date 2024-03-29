from rest_framework.generics import ListAPIView, RetrieveAPIView
from .services import BrandFilter, PaginationProducts, ProductFilter, ProductImageFilter, ProductSizeFilter
from .models import Brand, Category, Product, ProductImage
from .serializers import BrandSerializer, CategorySerializer, ProductDetailSerializer, ProductImageSerializer, ProductSerializer, NextPreviousProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from random import choice

# Create your views here.
class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None


class BrandListView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BrandFilter
    pagination_class = None


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = ProductFilter
    pagination_class = PaginationProducts
    ordering_fields = ['price', 'vendor_code', 'isRecommended', 'isNew']


class ProductListByIdView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PaginationProducts
    
    def get_queryset(self):
        ids = self.request.GET.getlist('ids')
        return self.queryset.filter(id__in=ids)
        


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = "pk"
    pagination_class = None


class ProductImageView(ListAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductImageFilter
    pagination_class = None

class ProductSearchView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PaginationProducts
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['vendor_code', 'keywords__title']
    ordering_fields = ['price', 'vendor_code', 'isRecommended', 'isNew']

class RandomProductView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = None
    
    def get_queryset(self):
        length = len(Product.objects.all())
        if length > 4:
           range_length = 4
        else:
            range_length = length
    
        products = []
        for i in range(0, range_length):
            product = choice(Product.objects.all())
            while product in products:
                product = choice(Product.objects.all())
            products.append(product)

        return products

class OnlyIdProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = NextPreviousProductSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = ProductFilter
    pagination_class = None
    ordering_fields = ['price', 'vendor_code', 'isRecommended', 'isNew']


class OnlyIdProductSearchView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = NextPreviousProductSerializer
    pagination_class = None
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['vendor_code', 'keywords__title']
    ordering_fields = ['price', 'vendor_code', 'isRecommended', 'isNew']


        
    

        