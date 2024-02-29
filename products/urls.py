from django.urls import path
from .views import PriceListCreateView, PriceRetrieveUpdateDestroyView, DiscountListCreateView, DiscountRetrieveUpdateDestroyView, DiscountScaleListCreateView, DiscountScaleRetrieveUpdateDestroyView, ProductListCreateView, ProductRetrieveUpdateDestroyView

urlpatterns = [
    #PRICE
    path('price/', PriceListCreateView.as_view(), name='price-list-create'),
    path('price/<uuid:pk>/', PriceRetrieveUpdateDestroyView.as_view(), name='price-detail'),
    #DISCOUNT
    path('discount/', DiscountListCreateView.as_view(), name='discount-list-create'),
    path('discount/<uuid:pk>/', DiscountRetrieveUpdateDestroyView.as_view(), name='discount-detail'),
    #DISCOUNT SCALE
    ##path('discount-scale/', DiscountScaleListCreateView.as_view(), name='discount-scale-list-create'), -- SOLO SE REGISTRA DESCUENTO
    ##path('discount-scale/<uuid:pk>/', DiscountScaleRetrieveUpdateDestroyView.as_view(), name='discount-scale-detail'), -- SOLO SE REGISTRA DESCUENTO
    #PRODUCT
    path('product/', ProductListCreateView.as_view(), name='product-list-create'),
    path('product/<uuid:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
]