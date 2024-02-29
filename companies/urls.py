from django.urls import path
from .views import CompanyListCreateView, CompanyRetrieveUpdateDestroyView, CompanyContactListCreateView, CompanyContactRetrieveUpdateDestroyView

urlpatterns = [
    #COMPANY
    path('company/', CompanyListCreateView.as_view(), name='company-scale-list-create'),
    path('company/<uuid:pk>/', CompanyRetrieveUpdateDestroyView.as_view(), name='company-scale-detail'),
    #COMPANY CONTACT
    path('company-contact/', CompanyContactListCreateView.as_view(), name='company-contact-list-create'),
    path('company-contact/<uuid:pk>/', CompanyContactRetrieveUpdateDestroyView.as_view(), name='company-contact-detail'),
]