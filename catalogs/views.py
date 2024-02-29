from catalogs.utils import STATUS_ACTIVO_DEFAULT, STATUS_ELIMINADO_DEFAULT, assign_default_status, get_status_instance
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import Country, Currency, InvoiceUse, PaymentCondition, ProductCategory, Status, State, City, Business, Platform, PaymentMethod, CompanyType, CompanySize, CompanyPhase, CampaignType, SubTypeActivity, TypeActivity, WayToPay
from .serializers import CurrencySerializer, InvoiceUseSerializer, PaymentConditionSerializer, ProductCategorySerializer, StatusSerializer, CountrySerializer, StateSerializer, CitySerializer, BusinessSerializer, PlatformSerializer, PaymentMethodSerializer, CompanyTypeSerializer, CompanyPhaseSerializer, CompanySizeSerializer, CampaignTypeSerializer, SubTypeActivitySerializer, TypeActivitySerializer, WayToPaySerializer

class StatusListCreateView(generics.ListCreateAPIView):
    queryset    = Status.objects.all()
    serializer_class    = StatusSerializer

class StatusRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def delete(self, request, *args, **kwargs):
        return Response({"message": "No es posible eliminar un estatus."}, status=status.HTTP_204_NO_CONTENT)

class CountryListCreateView(generics.ListCreateAPIView):
    serializer_class    = CountrySerializer

    def create(self, request, *args, **kwargs):
        #OBTENEMOS EL ESTATUS POR DEFAULT
        status_instance = get_status_instance(STATUS_ACTIVO_DEFAULT)
        serializer = CountrySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(status = status_instance)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        status_instance_active = get_status_instance(STATUS_ACTIVO_DEFAULT)
        queryset    = Country.objects.filter(status = status_instance_active)
        serializer = CountrySerializer(queryset, many=True)
        return Response(serializer.data)

class CountryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset    = Country.objects.all()
    serializer_class    = CountrySerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        status_instance_deleted = get_status_instance(STATUS_ELIMINADO_DEFAULT)
        instance.status = status_instance_deleted
        instance.save()

        return Response({"message": "El Pais se ha eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)

class StateListCreateView(generics.ListCreateAPIView):
    serializer_class    = StateSerializer

    def create(self, request, *args, **kwargs):
        #OBTENEMOS EL ESTATUS POR DEFAULT
        status_instance = get_status_instance(STATUS_ACTIVO_DEFAULT)
        serializer = StateSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(status = status_instance)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        status_instance_active = get_status_instance(STATUS_ACTIVO_DEFAULT)
        queryset    = State.objects.filter(status = status_instance_active)
        serializer = StateSerializer(queryset, many=True)
        return Response(serializer.data)

class StateRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset    = State.objects.all()
    serializer_class    = StateSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        status_instance_deleted = get_status_instance(STATUS_ELIMINADO_DEFAULT)
        instance.status = status_instance_deleted
        instance.save()

        return Response({"message": "El Estado se ha eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)

class CityListCreateView(generics.ListCreateAPIView):
    serializer_class    = CitySerializer

    def create(self, request, *args, **kwargs):
        #OBTENEMOS EL ESTATUS POR DEFAULT
        status_instance = get_status_instance(STATUS_ACTIVO_DEFAULT)
        serializer = CitySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(status = status_instance)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        status_instance_active = get_status_instance(STATUS_ACTIVO_DEFAULT)
        queryset    = City.objects.filter(status = status_instance_active)
        serializer = CitySerializer(queryset, many=True)
        return Response(serializer.data)

class CityRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset    = City.objects.all()
    serializer_class    = CitySerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        status_instance_deleted = get_status_instance(STATUS_ELIMINADO_DEFAULT)
        instance.status = status_instance_deleted
        instance.save()

        return Response({"message": "La Ciudad se ha eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)

class BusinessListCreateView(generics.ListCreateAPIView):
    serializer_class    = BusinessSerializer

    def create(self, request, *args, **kwargs):
        #OBTENEMOS EL ESTATUS POR DEFAULT
        status_instance = get_status_instance(STATUS_ACTIVO_DEFAULT)
        serializer = BusinessSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(status = status_instance)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        status_instance_active = get_status_instance(STATUS_ACTIVO_DEFAULT)
        queryset    = Business.objects.filter(status = status_instance_active)
        serializer = BusinessSerializer(queryset, many=True)
        return Response(serializer.data)

class BusinessRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset    = Business.objects.all()
    serializer_class    = BusinessSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        status_instance_deleted = get_status_instance(STATUS_ELIMINADO_DEFAULT)
        instance.status = status_instance_deleted
        instance.save()

        return Response({"message": "El Giro se ha eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)

class PlatformListCreateView(generics.ListCreateAPIView):
    serializer_class    = PlatformSerializer

    def create(self, request, *args, **kwargs):
        #OBTENEMOS EL ESTATUS POR DEFAULT
        status_instance = get_status_instance(STATUS_ACTIVO_DEFAULT)
        serializer = PlatformSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(status = status_instance)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        status_instance_active = get_status_instance(STATUS_ACTIVO_DEFAULT)
        queryset    = Platform.objects.filter(status = status_instance_active)
        serializer = PlatformSerializer(queryset, many=True)
        return Response(serializer.data)

class PlatformRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset    = Platform.objects.all()
    serializer_class    = PlatformSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        status_instance_deleted = get_status_instance(STATUS_ELIMINADO_DEFAULT)
        instance.status = status_instance_deleted
        instance.save()

        return Response({"message": "La Solución/Plataforma se ha eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)

class PaymentMethodListCreateView(generics.ListCreateAPIView):
    serializer_class    = PaymentMethodSerializer

    def create(self, request, *args, **kwargs):
        #OBTENEMOS EL ESTATUS POR DEFAULT
        status_instance = get_status_instance(STATUS_ACTIVO_DEFAULT)
        serializer = PaymentMethodSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(status = status_instance)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        status_instance_active = get_status_instance(STATUS_ACTIVO_DEFAULT)
        queryset    = PaymentMethod.objects.filter(status = status_instance_active)
        serializer = PaymentMethodSerializer(queryset, many=True)
        return Response(serializer.data)

class PaymentMethodRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset    = PaymentMethod.objects.all()
    serializer_class    = PaymentMethodSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        status_instance_deleted = get_status_instance(STATUS_ELIMINADO_DEFAULT)
        instance.status = status_instance_deleted
        instance.save()

        return Response({"message": "El tipo de pago se ha eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)

class CompanyTypeListCreateView(generics.ListCreateAPIView):
    serializer_class    = CompanyTypeSerializer

    def create(self, request, *args, **kwargs):
        #OBTENEMOS EL ESTATUS POR DEFAULT
        status_instance = get_status_instance(STATUS_ACTIVO_DEFAULT)
        serializer = CompanyTypeSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(status = status_instance)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        status_instance_active = get_status_instance(STATUS_ACTIVO_DEFAULT)
        queryset    = CompanyType.objects.filter(status = status_instance_active)
        serializer = CompanyTypeSerializer(queryset, many=True)
        return Response(serializer.data)

class CompanyTypeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset    = CompanyType.objects.all()
    serializer_class    = CompanyTypeSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        status_instance_deleted = get_status_instance(STATUS_ELIMINADO_DEFAULT)
        instance.status = status_instance_deleted
        instance.save()

        return Response({"message": "El tipo de empresa se ha eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)

class CompanySizeListCreateView(generics.ListCreateAPIView):
    serializer_class    = CompanySizeSerializer

    def create(self, request, *args, **kwargs):
        #OBTENEMOS EL ESTATUS POR DEFAULT
        status_instance = get_status_instance(STATUS_ACTIVO_DEFAULT)
        serializer = CompanySizeSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(status = status_instance)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        status_instance_active = get_status_instance(STATUS_ACTIVO_DEFAULT)
        queryset    = CompanySize.objects.filter(status = status_instance_active)
        serializer = CompanySizeSerializer(queryset, many=True)
        return Response(serializer.data)

class CompanySizeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset    = CompanySize.objects.all()
    serializer_class    = CompanySizeSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        status_instance_deleted = get_status_instance(STATUS_ELIMINADO_DEFAULT)
        instance.status = status_instance_deleted
        instance.save()

        return Response({"message": "El tamaño de empresa se ha eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)

class CompanyPhaseListCreateView(generics.ListCreateAPIView):
    serializer_class    = CompanyPhaseSerializer

    def create(self, request, *args, **kwargs):
        #OBTENEMOS EL ESTATUS POR DEFAULT
        status_instance = get_status_instance(STATUS_ACTIVO_DEFAULT)
        serializer = CompanyPhaseSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(status = status_instance)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        status_instance_active = get_status_instance(STATUS_ACTIVO_DEFAULT)
        queryset    = CompanyPhase.objects.filter(status = status_instance_active)
        serializer = CompanyPhaseSerializer(queryset, many=True)
        return Response(serializer.data)

class CompanyPhaseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset    = CompanyPhase.objects.all()
    serializer_class    = CompanyPhaseSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        status_instance_deleted = get_status_instance(STATUS_ELIMINADO_DEFAULT)
        instance.status = status_instance_deleted
        instance.save()

        return Response({"message": "La fase de empresa se ha eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)

class CampaignTypeListCreateView(generics.ListCreateAPIView):
    serializer_class    = CampaignTypeSerializer

    def create(self, request, *args, **kwargs):
        #OBTENEMOS EL ESTATUS POR DEFAULT
        status_instance = get_status_instance(STATUS_ACTIVO_DEFAULT)
        serializer = CampaignTypeSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(status = status_instance)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        status_instance_active = get_status_instance(STATUS_ACTIVO_DEFAULT)
        queryset    = CampaignType.objects.filter(status = status_instance_active)
        serializer = CampaignTypeSerializer(queryset, many=True)
        return Response(serializer.data)

class CampaignTypeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset    = CampaignType.objects.all()
    serializer_class    = CampaignTypeSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        status_instance_deleted = get_status_instance(STATUS_ELIMINADO_DEFAULT)
        instance.status = status_instance_deleted
        instance.save()

        return Response({"message": "El tipo de campaña se ha eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)
    
class ProductCategoryListCreateView(generics.ListCreateAPIView):
    serializer_class    = ProductCategorySerializer

    def create(self, request, *args, **kwargs):
        #OBTENEMOS EL ESTATUS POR DEFAULT
        status_instance = get_status_instance(STATUS_ACTIVO_DEFAULT)
        serializer = ProductCategorySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(status = status_instance)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        status_instance_active = get_status_instance(STATUS_ACTIVO_DEFAULT)
        queryset    = ProductCategory.objects.filter(status = status_instance_active)
        serializer = ProductCategorySerializer(queryset, many=True)
        return Response(serializer.data)

class ProductCategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset    = ProductCategory.objects.all()
    serializer_class    = ProductCategorySerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        status_instance_deleted = get_status_instance(STATUS_ELIMINADO_DEFAULT)
        instance.status = status_instance_deleted
        instance.save()

        return Response({"message": "La categoria de producto se ha eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)
    
class TypeActivityListCreateView(generics.ListCreateAPIView):
    serializer_class    = TypeActivitySerializer

    def create(self, request, *args, **kwargs):
        #OBTENEMOS EL ESTATUS POR DEFAULT
        status_instance = get_status_instance(STATUS_ACTIVO_DEFAULT)
        serializer = TypeActivitySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(status = status_instance)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        status_instance_active = get_status_instance(STATUS_ACTIVO_DEFAULT)
        queryset    = TypeActivity.objects.filter(status = status_instance_active)
        serializer = TypeActivitySerializer(queryset, many=True)
        return Response(serializer.data)

class TypeActivityRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset    = TypeActivity.objects.all()
    serializer_class    = TypeActivitySerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        status_instance_deleted = get_status_instance(STATUS_ELIMINADO_DEFAULT)
        instance.status = status_instance_deleted
        instance.save()

        return Response({"message": "La categoria de producto se ha eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)
    
class SubTypeActivityListCreateView(generics.ListCreateAPIView):
    serializer_class    = SubTypeActivitySerializer

    def create(self, request, *args, **kwargs):
        #OBTENEMOS EL ESTATUS POR DEFAULT
        status_instance = get_status_instance(STATUS_ACTIVO_DEFAULT)
        serializer = SubTypeActivitySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(status = status_instance)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        status_instance_active = get_status_instance(STATUS_ACTIVO_DEFAULT)
        queryset    = SubTypeActivity.objects.filter(status = status_instance_active)
        serializer = SubTypeActivitySerializer(queryset, many=True)
        return Response(serializer.data)

class SubTypeActivityRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset    = SubTypeActivity.objects.all()
    serializer_class    = SubTypeActivitySerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        status_instance_deleted = get_status_instance(STATUS_ELIMINADO_DEFAULT)
        instance.status = status_instance_deleted
        instance.save()

        return Response({"message": "La categoria de producto se ha eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)
    
class CurrencyListCreateView(generics.ListCreateAPIView):
    serializer_class    = CurrencySerializer

    def create(self, request, *args, **kwargs):
        #OBTENEMOS EL ESTATUS POR DEFAULT
        status_instance = get_status_instance(STATUS_ACTIVO_DEFAULT)
        serializer = CurrencySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(status = status_instance)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        status_instance_active = get_status_instance(STATUS_ACTIVO_DEFAULT)
        queryset    = Currency.objects.filter(status = status_instance_active)
        serializer = CurrencySerializer(queryset, many=True)
        return Response(serializer.data)

class CurrencyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset    = Currency.objects.all()
    serializer_class    = CurrencySerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        status_instance_deleted = get_status_instance(STATUS_ELIMINADO_DEFAULT)
        instance.status = status_instance_deleted
        instance.save()

        return Response({"message": "La moneda se ha eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)
    
class WayToPayListCreateView(generics.ListCreateAPIView):
    serializer_class    = WayToPaySerializer

    def create(self, request, *args, **kwargs):
        #OBTENEMOS EL ESTATUS POR DEFAULT
        status_instance = get_status_instance(STATUS_ACTIVO_DEFAULT)
        serializer = WayToPaySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(status = status_instance)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        status_instance_active = get_status_instance(STATUS_ACTIVO_DEFAULT)
        queryset    = WayToPay.objects.filter(status = status_instance_active)
        serializer = WayToPaySerializer(queryset, many=True)
        return Response(serializer.data)
    
class PaymentConditionListCreateView(generics.ListCreateAPIView):
    serializer_class    = PaymentConditionSerializer

    def create(self, request, *args, **kwargs):
        #OBTENEMOS EL ESTATUS POR DEFAULT
        status_instance = get_status_instance(STATUS_ACTIVO_DEFAULT)
        serializer = PaymentConditionSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(status = status_instance)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        status_instance_active = get_status_instance(STATUS_ACTIVO_DEFAULT)
        queryset    = PaymentCondition.objects.filter(status = status_instance_active)
        serializer = PaymentConditionSerializer(queryset, many=True)
        return Response(serializer.data)
    
class InvoiceUseListCreateView(generics.ListCreateAPIView):
    serializer_class    = InvoiceUseSerializer

    def create(self, request, *args, **kwargs):
        #OBTENEMOS EL ESTATUS POR DEFAULT
        status_instance = get_status_instance(STATUS_ACTIVO_DEFAULT)
        serializer = InvoiceUseSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(status = status_instance)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        status_instance_active = get_status_instance(STATUS_ACTIVO_DEFAULT)
        queryset    = InvoiceUse.objects.filter(status = status_instance_active)
        serializer = InvoiceUseSerializer(queryset, many=True)
        return Response(serializer.data)