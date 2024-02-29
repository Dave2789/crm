from django.urls import path
from .views import CampaignListCreateView, CampaignListSimple, CampaignRetrieveUpdateDestroyView

urlpatterns = [
    #CAMPAIGN
    path('campaign-list/', CampaignListSimple.as_view(), name='campaign-list-view'),
    path('campaign/', CampaignListCreateView.as_view(), name='campaign-list-create'),
    path('campaign/<uuid:pk>/', CampaignRetrieveUpdateDestroyView.as_view(), name='campaign-detail'),
    #CAMPAIGN USER
    #path('campaign-user/', CampaignUserListCreateView.as_view(), name='campaign-user-list-create'),
    #path('campaign-user/<uuid:pk>/', CampaignUserRetrieveUpdateDestroyView.as_view(), name='campaign-user-detail'),
    #CAMPAIGN COMPANY
    #path('campaign-company/', CampaignCompanyListCreateView.as_view(), name='campaign-companylist-create'),
    #path('campaign-company/<uuid:pk>/', CampaignCompanyRetrieveUpdateDestroyView.as_view(), name='campaign-company-detail'),
]
