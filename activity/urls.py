from django.urls import path
from .views import ActivityListCreateView, ActivityRetrieveUpdateDestroyView

urlpatterns = [
    path('activity/', ActivityListCreateView.as_view(), name='activity-list-create'),
    path('activity/<uuid:pk>/', ActivityRetrieveUpdateDestroyView.as_view(), name='activity-detail'),
]
