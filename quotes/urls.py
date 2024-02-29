from django.urls import path
from .views import QuoteInvoice, QuoteListCreateView, QuoteRetrieveUpdateDestroyView, QuoteOptionListCreateView, QuoteOptionRetrieveUpdateDestroyView, OptionProductListCreateView, OptionProductRetrieveUpdateDestroyView, QuoteTracking

urlpatterns = [
    #QUOTE
    path('quote/', QuoteListCreateView.as_view(), name='quote-list-create'),
    path('quote/<uuid:pk>/', QuoteRetrieveUpdateDestroyView.as_view(), name='quote-detail'),
    path('tracking/', QuoteTracking.as_view(), name='quote-tracking-create'),
    path('invoice/', QuoteInvoice.as_view(), name='quote-invoice-create'),
    #QUOTE OPTION --- SE CREA REGISTRO EN GENERAL
    ##path('quote-option/', QuoteOptionListCreateView.as_view(), name='company-phase-list-create'),
    ##path('quote-option/<uuid:pk>/', QuoteOptionRetrieveUpdateDestroyView.as_view(), name='company-phase-detail'),
    #OPTION PRODUCT
    ##path('option-product/', OptionProductListCreateView.as_view(), name='company-scale-list-create'),
    ##path('option-product/<uuid:pk>/', OptionProductRetrieveUpdateDestroyView.as_view(), name='company-scale-detail'),
]