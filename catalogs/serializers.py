from rest_framework import serializers
from .models import Currency, InvoiceUse, PaymentCondition, Status, Country, State, City, Business, Platform, PaymentMethod, CompanyType, CompanySize, CompanyPhase, CampaignType, ProductCategory, SubTypeActivity, TypeActivity, WayToPay

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Status
        #fields  = '__all__'
        exclude = ['created_at', 'update_at']
        read_only_fields    = ('status_id', ) 

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model   = Country
        #fields = '__all__'
        exclude = ['created_at', 'update_at', 'status']
        read_only_fields    = ('country_id', )

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model   = State
        #fields  = '__all__'
        exclude = ['created_at', 'update_at', 'status']
        read_only_fields    = ('state_id', )

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model   = City
        #fields  = '__all__'
        exclude = ['created_at', 'update_at', 'status']
        read_only_fields    = ('city_id', )

class BusinessSerializer(serializers.ModelSerializer):
    #status  =   StatusSerializer()
    class Meta:
        model   = Business
        #fields  = '__all__'
        exclude = ['created_at', 'update_at', 'status']
        read_only_fields    = ('business_id', )

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Platform
        #fields  = '__all__'
        exclude = ['created_at', 'update_at', 'status']
        read_only_fields    = ('platform_id', )

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model   = PaymentMethod
        #fields  = '__all__'
        exclude = ['created_at', 'update_at', 'status']
        read_only_fields    = ('payment_method_id', )

class CompanyTypeSerializer(serializers.ModelSerializer):
    #status  =   StatusSerializer()
    class Meta:
        model   = CompanyType
        #fields  = '__all__'
        exclude = ['created_at', 'update_at', 'status']
        read_only_fields    = ('company_type_id', )

class CompanySizeSerializer(serializers.ModelSerializer):
    class Meta:
        model   = CompanySize
        #fields   = '__all__'
        exclude = ['created_at', 'update_at', 'status']
        read_only_fields    = ('company_size_id', )

class CompanyPhaseSerializer(serializers.ModelSerializer):
    class Meta:
        model   = CompanyPhase
        #fields  = '__all__'
        exclude = ['created_at', 'update_at', 'status']
        read_only_fields    = ('company_phase_id', )

class CampaignTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model   = CampaignType
        #fields  =   '__all__'
        exclude = ['created_at', 'update_at', 'status']
        read_only_fields    = ('campaign_type_id', )

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model   = ProductCategory
        #fields  = '__all__'
        exclude = ['created_at', 'update_at', 'status']
        read_only_fields    = ('product_category_id', )

class TypeActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model   = TypeActivity
        #fields  = '__all__'
        exclude = ['created_at', 'update_at', 'status']
        read_only_fields    = ('type_activity_id', )

class SubTypeActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model   = SubTypeActivity
        #fields  = '__all__'
        exclude = ['created_at', 'update_at', 'status']
        read_only_fields    = ('sub_type_activity_id', )

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model   = Currency
        #fields  = '__all__'
        exclude = ['created_at', 'update_at', 'status']
        read_only_fields    = ('currency_id', )

class WayToPaySerializer(serializers.ModelSerializer):
    class Meta:
        model   = WayToPay
        #fields  = '__all__'
        exclude = ['created_at', 'update_at', 'status']
        read_only_fields    = ('way_to_pay_id', )

class PaymentConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model   = PaymentCondition
        #fields  = '__all__'
        exclude = ['created_at', 'update_at', 'status']
        read_only_fields    = ('payment_condition_id', )

class InvoiceUseSerializer(serializers.ModelSerializer):
    class Meta:
        model   = InvoiceUse
        #fields  = '__all__'
        exclude = ['created_at', 'update_at', 'status']
        read_only_fields    = ('invoice_use_id', )