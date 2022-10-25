from rest_framework.generics import ListAPIView, RetrieveAPIView
from .services import BrandFilter, PaginationProducts, ProductFilter, ProductImageFilter, ProductSizeFilter
from .models import Brand, Category, Product, ProductImage, ProductSize
from .serializers import BrandSerializer, CategorySerializer, ProductDetailSerializer, ProductImageSerializer, ProductSerializer, ProductSizesSerializer
from django_filters.rest_framework import DjangoFilterBackend

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
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter
    pagination_class = PaginationProducts


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

class ProductSizesView(ListAPIView):
    queryset = ProductSize.objects.all()
    serializer_class = ProductSizesSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductSizeFilter
    pagination_class = None