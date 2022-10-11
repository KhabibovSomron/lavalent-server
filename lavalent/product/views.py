from rest_framework.generics import ListAPIView, RetrieveAPIView
from .services import BrandFilter, ProductFilter
from .models import Brand, Category, Product
from .serializers import BrandSerializer, CategorySerializer, ProductDetailSerializer, ProductSerializer
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