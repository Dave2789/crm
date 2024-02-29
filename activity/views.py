from catalogs.utils import STATUS_ACTIVO_DEFAULT, STATUS_ELIMINADO_DEFAULT, get_status_instance
from .serializers import ActivitySerializer
from .models import Activity
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class ActivityListCreateView(generics.ListCreateAPIView):
    serializer_class    = ActivitySerializer

    # -------------- FILTROS
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name = 'status_id',
                in_ = openapi.IN_QUERY,
                required = False,
                type = openapi.TYPE_STRING,
                description = "UUID Estatus para filtrar"
            ),
            openapi.Parameter(
                name = 'user_id',
                in_ = openapi.IN_QUERY,
                required = False,
                type = openapi.TYPE_STRING,
                description = "UUID de agente para filtrar"
            ),
            openapi.Parameter(
                name = 'activity_type_id',
                in_ = openapi.IN_QUERY,
                required = False,
                type = openapi.TYPE_STRING,
                description = "UUID tipo de actividad para filtrar"
            ),
            openapi.Parameter(
                name='start_date',
                in_=openapi.IN_QUERY,
                required=False,
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_DATE,
                description="Fecha inicio para filtrar (formato: 'YYYY-MM-DD')"
            ),
            openapi.Parameter(
                name='end_date',
                in_=openapi.IN_QUERY,
                required=False,
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_DATE,
                description="Fecha final para filtrar (formato: 'YYYY-MM-DD')"
            )
        ]
    )

    def get(self, request, *args, **kwargs):
        status_instance_active = get_status_instance(STATUS_ACTIVO_DEFAULT)
        queryset    = Activity.objects.filter(status = status_instance_active)
        serializer = ActivitySerializer(queryset, many=True)
        return Response(serializer.data)
    
    def get_queryset(self):
        status_instance_active = get_status_instance(STATUS_ACTIVO_DEFAULT)
        queryset    = Activity.objects.filter(status = status_instance_active)
        #Obtengo parametros para filtrar
        status          = self.request.query_params.get('status_id', None)
        user            = self.request.query_params.get('user_id', None)
        activity_type_id   = self.request.query_params.get('activity_type_id', None)
        start_date      = self.request.query_params.get('start_date', None)
        end_date        = self.request.query_params.get('end_date', None)

        #Verificamos tipo de filtro, en caso de que no exista alguno retornara todo.
        if status is not None:
            queryset = Activity.objects.all()
            queryset = queryset.filter(status = status)
        if activity_type_id is not None:
            queryset = queryset.filter(activity_type = activity_type_id)
        if user is not None:
            queryset
        if start_date is not None and end_date is not None:
            queryset = queryset.filter(start_date__gte = start_date, end_date__lte = end_date)
        
        #Retornamos filtro
        return queryset

    def create(self, request, *args, **kwargs):
        #OBTENEMOS EL ESTATUS POR DEFAULT
        status_instance = get_status_instance(STATUS_ACTIVO_DEFAULT)
        serializer = ActivitySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(status = status_instance)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ActivityRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset    = Activity.objects.all()
    serializer_class    = ActivitySerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        status_instance_deleted = get_status_instance(STATUS_ELIMINADO_DEFAULT)
        instance.status = status_instance_deleted
        instance.save()

        return Response({"message": "La actividad se ha eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)
    
