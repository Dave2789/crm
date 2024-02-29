from django.urls import path
from . import views

urlpatterns = [
    path('emails/', views.EmailList.as_view(), name='email-list'),
    #path('emails/<int:pk>/', views.EmailDetail.as_view(), name='email-detail'),
    # Otros endpoints de la API si es necesario
]