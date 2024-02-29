from rest_framework.exceptions import ValidationError
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from drf_yasg import openapi
from rest_framework.views import APIView
from .models import Campaign, CampaignUser, CampaignCompany
from companies.models import Company
from users.models import CustomUser
from .serializers import CampaignCompanySerializer, CampaignInsertSerializer, CampaignListSerializer, CampaignSerializer, CampaignUserSerializer
from users.serializers import UserSerializer
from companies.serializers import CompanySerializer
from django.shortcuts import get_object_or_404
from catalogs.utils import STATUS_ACTIVO_DEFAULT, STATUS_ELIMINADO_DEFAULT, get_status_instance
from django.db import transaction

class CampaignListCreateView(generics.ListCreateAPIView):
    serializer_class    = CampaignSerializer
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
                name = 'campaign_type_id',
                in_ = openapi.IN_QUERY,
                required = False,
                type = openapi.TYPE_STRING,
                description = "UUID tipo de campaña para filtrar"
            ),
            openapi.Parameter(
                name = 'user_id',
                in_ = openapi.IN_QUERY,
                required = False,
                type = openapi.TYPE_STRING,
                description = "UUID de agente para filtrar"
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
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        status_instance_active = get_status_instance(STATUS_ACTIVO_DEFAULT)
        queryset    = Campaign.objects.filter(status = status_instance_active)
        #Obtengo parametros para filtrar
        status          = self.request.query_params.get('status_id', None)
        campaign_type   = self.request.query_params.get('campaign_type_id', None)
        user            = self.request.query_params.get('user_id', None)
        start_date      = self.request.query_params.get('start_date', None)
        end_date        = self.request.query_params.get('end_date', None)

        #Verificamos tipo de filtro, en caso de que no exista alguno retornara todo.
        if status is not None:
            queryset = queryset.filter(status = status)
        if campaign_type is not None:
            queryset = queryset.filter(campaign_type = campaign_type)
        if user is not None:
            queryset
        if start_date is not None and end_date is not None:
            queryset = queryset.filter(start_date__gte = start_date, end_date__lte = end_date)
        
        #Retornamos filtro
        return queryset
    
    def create(self, request, *args, **kwargs):
        serializer = CampaignInsertSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        #OBTENEMOS EL ESTATUS POR DEFAULT
        status_instance = get_status_instance(STATUS_ACTIVO_DEFAULT)
        try:
            with transaction.atomic():

                campaign_instance = serializer.save(status = status_instance)
                companies_data = request.data.get('companies', [])
                users_data = request.data.get('users', [])

                for company_data in companies_data:
                    company_instance = get_object_or_404(Company, company_id=company_data)
                    CampaignCompany.objects.create(campaign=campaign_instance, company=company_instance, status=status_instance)

                for user_data in users_data:
                    user_instance = get_object_or_404(CustomUser, id=user_data)
                    CampaignUser.objects.create(campaign=campaign_instance, user=user_instance, status=status_instance)

        except ValidationError as e:
            return Response({'detail': 'Error de validación: ' + str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'detail': 'Error interno del servidor: ' + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        campaign_serializer = CampaignSerializer(campaign_instance)
        return Response(campaign_serializer.data, status=status.HTTP_201_CREATED)

class CampaignRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset    = Campaign.objects.all()
    serializer_class    = CampaignSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data = request.data, partial = True)
        serializer.is_valid(raise_exception = True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def patch(self, request, pk):
        try:
            companies_data = request.data.get('companies', [])
            users_data = request.data.get('users', [])
            campaign_id = pk

            # Obtener campaña
            campaign = get_object_or_404(Campaign, campaign_id = campaign_id)

            #OBTENEMOS LOS ESTATUS POR DEFAULT
            status_instance_active = get_status_instance(STATUS_ACTIVO_DEFAULT)
            status_instance_inactive = get_status_instance(STATUS_ELIMINADO_DEFAULT)

            for company in companies_data:
                try:
                    company_instance = get_object_or_404(Company, company_id = company)
                    campaign_company = CampaignCompany.objects.get(campaign = campaign, company = company_instance)
                    campaign_company.status = status_instance_active
                    campaign_company.save()
                except CampaignCompany.DoesNotExist:
                    # Si la compañía no existe, crearla
                    CampaignCompany.objects.create(campaign = campaign, company = company_instance, status = status_instance_active)

            for user in users_data:
                try:
                    user_instance = get_object_or_404(CustomUser, id = user)
                    user_company = CampaignUser.objects.get(campaign = campaign, user = user_instance)
                    user_company.status = status_instance_active
                    user_company.save()
                except CampaignUser.DoesNotExist:
                    # Si el usuario no existe, crearlo
                    CampaignUser.objects.create(campaign = campaign, user = user_instance, status = status_instance_active)


            # Actualizar datos de la campaña
            campaign_serializer = CampaignInsertSerializer(campaign, data=request.data, partial=True)
            if campaign_serializer.is_valid():
                campaign_serializer.save()

            # Actualizar estados inactivos
            CampaignCompany.objects.exclude(company_id__in=companies_data).update(status=status_instance_inactive)
            CampaignUser.objects.exclude(user_id__in=users_data).update(status=status_instance_inactive)

            '''campaign_data = request.data()
            for key, value in campaign_data.items():
                setattr(campaign, key, value)
            campaign.save()

            inactive_companies = CampaignCompany.objects.exclude(campaign_id__in = companies_data)
            inactive_users = CampaignUser.objects.exclude(user_id__in = users_data)

            for company in inactive_companies:
                company.status = status_instance_inactive
                company.save()

            for user in inactive_users:
                user.status = status_instance_inactive
                user.save()
            
            campaign_serializer = CampaignSerializer(campaign)'''
            return Response(campaign_serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        status_instance_deleted = get_status_instance(STATUS_ELIMINADO_DEFAULT)
        instance.status = status_instance_deleted
        instance.save()

        return Response({"message": "La campaña se ha eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)

class CampaignUserListCreateView(generics.ListCreateAPIView):
    queryset    = CampaignUser.objects.all()
    serializer_class    = CampaignUserSerializer

class CampaignUserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset    = CampaignUser.objects.all()
    serializer_class    = CampaignUserSerializer

class CampaignCompanyListCreateView(generics.ListCreateAPIView):
    queryset    = CampaignCompany.objects.all()
    serializer_class    = CampaignCompanySerializer

class CampaignCompanyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset    = CampaignCompany.objects.all()
    serializer_class    = CampaignCompanySerializer

class CampaignListSimple(APIView):
    def get(self, request):
        status_instance_active = get_status_instance(STATUS_ACTIVO_DEFAULT)
        queryset = Campaign.objects.all()
        serializer = CampaignListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)