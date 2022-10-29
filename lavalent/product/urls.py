from django.urls import path
from . import views


urlpatterns = [
    path('categorylist/', views.CategoryListView.as_view()),
    path('brandlist/', views.BrandListView.as_view()),
    path('productlist/', views.ProductListView.as_view()),
    path('randomproduct/', views.RandomProductView.as_view()),
    path('productdetail/<int:pk>/', views.ProductDetailView.as_view()),
    path('productimagelist/', views.ProductImageView.as_view()),
    path('productsizes/', views.ProductSizesView.as_view()),
    path('productlist-by-id/', views.ProductListByIdView.as_view()),
    path('search/', views.ProductSearchView.as_view()),
    path('brand/<int:pk>/', views.ProductSearchView.as_view()),


    
]