from rest_framework.generics import ListAPIView, RetrieveAPIView
from .services import BrandFilter, ProductFilter, ProductImageFilter
from .models import Brand, Category, Product, ProductImage
from .serializers import BrandSerializer, CategorySerializer, ProductDetailSerializer, ProductImageSerializer, ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BrandListView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BrandFilter


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = "pk"


class ProductImageView(ListAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductImageFilter