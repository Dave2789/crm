from django.urls import path
from .views import dashboard_graphics, dashboard_products, dashboard_statics

urlpatterns = [
    path('statics/', dashboard_statics, name='dashboard-statics'),
    path('graphics/', dashboard_graphics, name='dashboard-graphics'),
    path('products/', dashboard_products, name='dashboard-products'),
]