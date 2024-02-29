from django.db import transaction
from catalogs.utils import STATUS_ACTIVO_DEFAULT, get_status_instance
from rest_framework.exceptions import ValidationError
from rest_framework import generics
from drf_yasg import openapi
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from django.utils.text import slugify
from .models import Company, CompanyContact
from .serializers import CompanyInsertSerializer, CompanySerializer, CompanyContactSerializer

class CompanyListCreateView(generics.ListCreateAPIView):
    serializer_class = CompanySerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name = 'company_type_id',
                in_ = openapi.IN_QUERY,
                required = False,
                type = openapi.TYPE_STRING,
                description = "UUID Tipo de empresa para filtrar"
            ),
            openapi.Parameter(
                name = 'business_id',
                in_ = openapi.IN_QUERY,
                required = False,
                type = openapi.TYPE_STRING,
                description = "UUID del giro de negocio para filtrar"
            ),
            openapi.Parameter(
                name = 'status_id',
                in_ = openapi.IN_QUERY,
                required = False,
                type = openapi.TYPE_STRING,
                description = "UUID del estatus para filtrar"
            ),
            openapi.Parameter(
                name = 'campaign_id',
                in_ = openapi.IN_QUERY,
                required = False,
                type = openapi.TYPE_STRING,
                description = "UUID de la campaña para filtrar"
            ),
            openapi.Parameter(
                name='register_date_start',
                in_=openapi.IN_QUERY,
                required=False,
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_DATE,
                description="Fecha de registro para filtrar (formato: 'YYYY-MM-DD')"
            ),
            openapi.Parameter(
                name='register_date_end',
                in_=openapi.IN_QUERY,
                required=False,
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_DATE,
                description="Fecha de registro para filtrar (formato: 'YYYY-MM-DD')"
            ),
            openapi.Parameter(
                name='company_phase',
                in_=openapi.IN_QUERY,
                required=False,
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_DATE,
                description="UUID Fase de empresa, Prospecto, Lead, Cliente"
            )
        ]
    )
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Company.objects.all()
        #Obtengo parametros para filtrar
        company_type    =   self.request.query_params.get('company_type_id', None)
        business    =   self.request.query_params.get('business_id', None)
        status      =   self.request.query_params.get('status_id', None)
        campaign    =   self.request.query_params.get('campaign_id', None)
        register_date_start =   self.request.query_params.get('register_date_start', None)
        register_date_end   =   self.request.query_params.get('register_date_end', None)
        company_phase       =   self.request.query_params.get('company_phase', None)

        #Verificamos tipo de filtro, en caso de que no exista alguno retornara todo.
        if company_type is not None:
            queryset = queryset.filter(company_type = company_type)
        if business is not None:
            queryset = queryset.filter(business = business)
        if status is not None:
            queryset = queryset.filter(status = status)
        if campaign is not None:
            queryset = queryset.filter(campaign = campaign)
        if register_date_start is not None and register_date_end is not None:
            queryset = queryset.filter(register_date__gte = register_date_start, register_date__lte = register_date_end)
        if company_phase is not None:
            queryset = queryset.filter(company_phase = company_phase)

        #Retornamos filtro
        return queryset

    def create(self, request, *args, **kwargs):
        #OBTENEMOS EL ESTATUS POR DEFAULT
        status_instance = get_status_instance(STATUS_ACTIVO_DEFAULT)

        try:
            with transaction.atomic():

                serializer  = CompanyInsertSerializer(data = request.data)
                serializer.is_valid(raise_exception=True)
                company_instance = serializer.save(status = status_instance)
                company_contacts = request.data.get('company_contacts', [])
                for contact in company_contacts:
                    company_contact_instance = CompanyContactSerializer(data = contact)
                    company_contact_instance.is_valid(raise_exception=True)
                    company_contact_instance.save(company = company_instance, status = status_instance)

        except ValidationError as e:
            return Response({'detail': 'Error de validación: ' + str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'detail': 'Error interno del servidor: ' + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        company_serializer = CompanySerializer(company_instance)
        return Response(company_serializer.data, status = status.HTTP_201_CREATED)

class CompanyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset    = Company.objects.all()
    serializer_class    = CompanySerializer

    def delete(self, request, *args, **kwargs):
        return Response({"message": "No se permite eliminar el objeto"}, status = status.HTTP_405_METHOD_NOT_ALLOWED)

class CompanyContactListCreateView(generics.ListCreateAPIView):
    queryset    = CompanyContact.objects.all()
    serializer_class    = CompanyContactSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name = 'company_id',
                in_ = openapi.IN_QUERY,
                required = False,
                type = openapi.TYPE_STRING,
                description = "UUID empresa para filtrar"
            ),
        ]
    )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = CompanyContact.objects.all()
        #Obtengo parametros para filtrar
        company    =   self.request.query_params.get('company_id', None)

        #Verificamos tipo de filtro, en caso de que no exista alguno retornara todo.
        if company is not None:
            queryset = queryset.filter(company = company)

        #Retornamos filtro
        return queryset

class CompanyContactRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset    = CompanyContact.objects.all()
    serializer_class    = CompanyContactSerializer