from catalogs.utils import STATUS_ACTIVO_DEFAULT, get_status_instance
from rest_framework import serializers
from .models import Campaign, CampaignUser, CampaignCompany
from users.serializers import UserSerializer
from users.models import CustomUser
from companies.serializers import CompanySerializer
from catalogs.models import CampaignType, ProductCategory
from catalogs.serializers import CampaignTypeSerializer, ProductCategorySerializer

class CampaignSerializer(serializers.ModelSerializer):
    #status_instance = get_status_instance(STATUS_ACTIVO_DEFAULT)
    #users           = serializers.PrimaryKeyRelatedField(many = True, queryset = CampaignUser.objects.filter(status = status_instance), allow_null = True)
    #companies       = serializers.PrimaryKeyRelatedField(many = True, queryset = CampaignCompany.objects.filter(status = status_instance), allow_null = True)
    campaign_type   = serializers.PrimaryKeyRelatedField(queryset = CampaignType.objects.all(), allow_null=True)
    owner_user      = serializers.PrimaryKeyRelatedField(queryset = CustomUser.objects.all(), allow_null=True)
    product_category    = serializers.PrimaryKeyRelatedField(queryset = ProductCategory.objects.all(), allow_null=True)

    class Meta:
        model   = Campaign
        #fields  = '__all__'
        exclude = ['created_at', 'update_at', 'status']
        read_only_fields    = ('campaign_id', )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['companies']     = CampaignCompanySerializer(instance.companies.all(), many = True).data
        representation['users']         = CampaignUserSerializer(instance.users.all(), many = True).data
        representation['campaign_type'] = CampaignTypeSerializer(instance.campaign_type).data
        representation['owner_user']    = UserSerializer(instance.owner_user).data
        representation['product_category']  = ProductCategorySerializer(instance.product_category).data

        return representation

class CampaignUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model   = CampaignUser
        fields  = '__all__'
        read_only_fields    = ('campaign_user_id', 'user', )

class CampaignCompanySerializer(serializers.ModelSerializer):
    company = CompanySerializer() 
    class Meta:
        model   = CampaignCompany
        fields  = '__all__'
        read_only_fields    = ('campaign_company_id', 'company', )

class CampaignInsertSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Campaign
        fields  = '__all__'
        read_only_fields    = ('campaign_company_id', )

class CampaignListSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Campaign
        fields  = 'campaign_id', 'campaign_name', 'campaign_code',
        read_only_fields    = ('campaign_id', 'campaign_name', 'campaign_code', )