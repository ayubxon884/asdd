from django.urls import path
from .views import *

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('products/',ProductListView.as_view(),name='products'),
    path('product/<int:pk>/',ProductDetailView.as_view(),name='product_detail'),
    path('product/new/', ProductCreateView.as_view(),name='product_new'),
    path('product/<int:pk>/edit', ProductUpdateView.as_view(),name='product_edit'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(),name='product_delete'),
]