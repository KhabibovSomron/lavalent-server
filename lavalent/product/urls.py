from django.urls import path
from . import views


urlpatterns = [
    path('categorylist/', views.CategoryListView.as_view()),
    path('brandlist/', views.BrandListView.as_view()),
    path('productlist/', views.ProductListView.as_view()),
    path('productdetail/<int:pk>/', views.ProductDetailView.as_view()),
    path('productimagelist/', views.ProductImageView.as_view()),
]