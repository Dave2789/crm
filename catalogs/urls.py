from django.urls import path
from .views import CampaignTypeListCreateView, CampaignTypeRetrieveUpdateDestroyView, CompanyPhaseListCreateView, CompanyPhaseRetrieveUpdateDestroyView, CompanySizeListCreateView, CompanySizeRetrieveUpdateDestroyView, CompanyTypeListCreateView, CompanyTypeRetrieveUpdateDestroyView, CurrencyListCreateView, CurrencyRetrieveUpdateDestroyView, InvoiceUseListCreateView, PaymentConditionListCreateView, PaymentMethodListCreateView, PaymentMethodRetrieveUpdateDestroyView, ProductCategoryListCreateView, ProductCategoryRetrieveUpdateDestroyView, StatusListCreateView, StatusRetrieveUpdateDestroyView, CountryListCreateView, CountryRetrieveUpdateDestroyView, StateListCreateView, StateRetrieveUpdateDestroyView, CityListCreateView, CityRetrieveUpdateDestroyView, BusinessListCreateView, BusinessRetrieveUpdateDestroyView, PlatformListCreateView, PlatformRetrieveUpdateDestroyView, SubTypeActivityListCreateView, SubTypeActivityRetrieveUpdateDestroyView, TypeActivityListCreateView, TypeActivityRetrieveUpdateDestroyView, WayToPayListCreateView

urlpatterns = [
    #STATUS
    path('status/', StatusListCreateView.as_view(), name='status-list-create'),
    #path('status/<uuid:pk>/', StatusRetrieveUpdateDestroyView.as_view(), name='status-detail'),
    #COUNTRY
    path('country/', CountryListCreateView.as_view(), name='country-list-create'),
    path('country/<uuid:pk>/', CountryRetrieveUpdateDestroyView.as_view(), name='country-detail'),
    #STATE
    path('state/', StateListCreateView.as_view(), name='state-list-create'),
    path('state/<uuid:pk>/', StateRetrieveUpdateDestroyView.as_view(), name='state-detail'),
    #CITY
    path('city/', CityListCreateView.as_view(), name='city-list-create'),
    path('city/<uuid:pk>/', CityRetrieveUpdateDestroyView.as_view(), name='city-detail'),
    #BUSINESS
    path('business/', BusinessListCreateView.as_view(), name='business-list-create'),
    path('business/<uuid:pk>/', BusinessRetrieveUpdateDestroyView.as_view(), name='business-detail'),
    #PLATFORM
    path('platform/', PlatformListCreateView.as_view(), name='platform-list-create'),
    path('platform/<uuid:pk>/', PlatformRetrieveUpdateDestroyView.as_view(), name='platform-detail'),
    #COMPANY TYPE
    path('company-type/', CompanyTypeListCreateView.as_view(), name='company-type-list-create'),
    path('company-type/<uuid:pk>/', CompanyTypeRetrieveUpdateDestroyView.as_view(), name='company-type-detail'),
    #COMPANY SIZE
    path('company-size/', CompanySizeListCreateView.as_view(), name='company-size-list-create'),
    path('company-size/<uuid:pk>/', CompanySizeRetrieveUpdateDestroyView.as_view(), name='company-size-detail'),
    #COMPANY PHASE
    ##path('company-phase/', CompanyPhaseListCreateView.as_view(), name='company-phase-list-create'), -- SOLO USO INTERNO
    ##path('company-phase/<uuid:pk>/', CompanyPhaseRetrieveUpdateDestroyView.as_view(), name='company-phase-detail'), -- SOLO USO INTERNO
    #CAMPAIGN TYPE
    path('campaign-type/', CampaignTypeListCreateView.as_view(), name='campaign-type-list-create'),
    path('campaign-type/<uuid:pk>/', CampaignTypeRetrieveUpdateDestroyView.as_view(), name='campaign-type-detail'),
    #PRODUCT CATEGORY
    path('product-category/', ProductCategoryListCreateView.as_view(), name='product-category-list-create'),
    path('product-category/<uuid:pk>/', ProductCategoryRetrieveUpdateDestroyView.as_view(), name='product-category-detail'),
    #PAYMENT METHOD
    path('payment-method/', PaymentMethodListCreateView.as_view(), name='payment-method-list-create'),
    path('payment-method/<uuid:pk>/', PaymentMethodRetrieveUpdateDestroyView.as_view(), name='payment-method-detail'),
    #TYPE ACTIVITY
    path('activity-type/', TypeActivityListCreateView.as_view(), name='activity-type-list-create'),
    path('activity-type/<uuid:pk>/', TypeActivityRetrieveUpdateDestroyView.as_view(), name='activity-type-detail'),
    #SUB TYPE ACTIVITY
    path('activity-subtype/', SubTypeActivityListCreateView.as_view(), name='activity-type-list-create'),
    path('activity-subtype/<uuid:pk>/', SubTypeActivityRetrieveUpdateDestroyView.as_view(), name='activity-type-detail'),
    #CURRENCY
    path('currency/', CurrencyListCreateView.as_view(), name='currency-list-create'),
    path('currency/<uuid:pk>/', CurrencyRetrieveUpdateDestroyView.as_view(), name='currency-detail'),
    #
    path('way-to-pay/', WayToPayListCreateView.as_view(), name='way-to-pay-list-create'),
    path('payment-condition/', PaymentConditionListCreateView.as_view(), name='payment-condition-list-create'),
    path('invoice-use/', InvoiceUseListCreateView.as_view(), name='invoice-use-list-create'),
]
