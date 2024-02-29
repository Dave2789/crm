from rest_framework import generics
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers import UserSerializer
from .models import CustomUser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class LoginView(APIView):

    @swagger_auto_schema(
        request_body = openapi.Schema(
            type = openapi.TYPE_OBJECT,
            required = ['email', 'password'],
            properties = {
                'email': openapi.Schema(type = openapi.TYPE_STRING),
                'password': openapi.Schema(type = openapi.TYPE_STRING)
            },
        ),
        operation_description="Correo y contraseña"
    )

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({'error': 'Por favor ingrese correo y contraseña.'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(email=email, password=password)

        if user:
            login(request, user)
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Correo o contraseña incorrecta.'}, status=status.HTTP_404_NOT_FOUND)

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)

class UserListCreateView(generics.ListCreateAPIView):
    queryset    = CustomUser.objects.all()
    serializer_class    = UserSerializer

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset    = CustomUser.objects.all()
    serializer_class    = UserSerializer

    def delete(self, request, *args, **kwargs):
        return Response({"message": "No se permite eliminar el objeto"}, status = status.HTTP_405_METHOD_NOT_ALLOWED)