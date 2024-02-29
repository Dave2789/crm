from rest_framework import serializers
from .models import Company, CompanyContact
from catalogs.serializers import CompanyTypeSerializer, BusinessSerializer, CountrySerializer, InvoiceUseSerializer, PaymentConditionSerializer, PaymentMethodSerializer, StateSerializer, CitySerializer, PlatformSerializer, CompanySizeSerializer, CompanyPhaseSerializer, WayToPaySerializer
from catalogs.models import CompanyType, Business, Country, InvoiceUse, PaymentCondition, PaymentMethod, State, City, Platform, CompanySize, CompanyPhase, WayToPay
from users.models import CustomUser
from users.serializers import UserSerializer

class CompanyContactSerializer(serializers.ModelSerializer):
    class Meta:
        model   = CompanyContact
        #fields  = '__all__'
        exclude = ['created_at', 'update_at', 'status']
        read_only_fields    = ('contact_id', )

class CompanySerializer(serializers.ModelSerializer):
    company_type    = serializers.PrimaryKeyRelatedField(queryset = CompanyType.objects.all(), allow_null=True)
    business        = serializers.PrimaryKeyRelatedField(queryset = Business.objects.all(), allow_null=True)
    owner_user      = serializers.PrimaryKeyRelatedField(queryset = CustomUser.objects.all(), allow_null=True)
    country         = serializers.PrimaryKeyRelatedField(queryset = Country.objects.all(), allow_null=True)
    state           = serializers.PrimaryKeyRelatedField(queryset = State.objects.all(), allow_null=True)
    city            = serializers.PrimaryKeyRelatedField(queryset = City.objects.all(), allow_null=True)
    platform        = serializers.PrimaryKeyRelatedField(queryset = Platform.objects.all(), allow_null=True)
    company_size    = serializers.PrimaryKeyRelatedField(queryset = CompanySize.objects.all(), allow_null=True)
    company_phase   = serializers.PrimaryKeyRelatedField(queryset = CompanyPhase.objects.all(), allow_null=True)
    payment_method  = serializers.PrimaryKeyRelatedField(queryset = PaymentMethod.objects.all(), allow_null=True)
    way_to_pay      = serializers.PrimaryKeyRelatedField(queryset = WayToPay.objects.all(), allow_null=True)
    payment_condition   = serializers.PrimaryKeyRelatedField(queryset = PaymentCondition.objects.all(), allow_null=True)
    invoice_use     = serializers.PrimaryKeyRelatedField(queryset = InvoiceUse.objects.all(), allow_null=True)

    company_contacts    = CompanyContactSerializer(many=True, read_only=True)
    
    class Meta:
        model   = Company
        #fields  = '__all__'
        exclude = ['created_at', 'update_at', 'status']
        read_only_fields    = ('company_id', )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        company_contacts = instance.companycontact_set.all()
        data['company_contacts'] = CompanyContactSerializer(company_contacts, many=True).data

        if instance.company_type is not None:
            data['company_type']    = CompanyTypeSerializer(instance.company_type).data
        if instance.business is not None:
            data['business']        = BusinessSerializer(instance.business).data
        if instance.owner_user is not None:
            data['owner_user']      = UserSerializer(instance.owner_user).data
        if instance.country is not None:
            data['country']         = CountrySerializer(instance.country).data
        if instance.state is not None:
            data['state']           = StateSerializer(instance.state).data
        if instance.city is not None:
            data['city']            = CitySerializer(instance.city).data
        if instance.platform is not None:
            data['platform']        = PlatformSerializer(instance.platform).data
        if instance.company_size is not None:
            data['company_size']    = CompanySizeSerializer(instance.company_size).data
        if instance.company_phase is not None:
            data['company_phase']   = CompanyPhaseSerializer(instance.company_phase).data
        if instance.payment_method is not None:
            data['payment_method']  = PaymentMethodSerializer(instance.payment_method).data
        if instance.way_to_pay is not None:
            data['way_to_pay']      = WayToPaySerializer(instance.way_to_pay).data
        if instance.payment_condition is not None:
            data['payment_condition']   = PaymentConditionSerializer(instance.payment_condition).data
        if instance.invoice_use is not None:
            data['invoice_use']   = InvoiceUseSerializer(instance.invoice_use).data

        return data
    
class CompanyInsertSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Company
        fields  = '__all__'
        read_only_fields    = ('company_id', )