from django.urls import path
from .views import LoginView, LogoutView, UserListCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
    #LOGIN / LOGOUT
    path('login/', LoginView.as_view(), name='auth-login'),
    path('logout/', LogoutView.as_view(), name='auth-logout'),
    #USERS
    path('user/', UserListCreateView.as_view(), name='user-list-create'),
    path('user/<uuid:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
]
