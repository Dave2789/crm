from campaigns.models import Campaign
from campaigns.serializers import CampaignSerializer
from catalogs.models import TypeActivity
from catalogs.serializers import TypeActivitySerializer
from companies.models import Company
from companies.serializers import CompanySerializer
from users.models import CustomUser
from users.serializers import UserSerializer
from .models import Activity
from rest_framework import serializers

class ActivitySerializer(serializers.ModelSerializer):
    type_activity   = serializers.PrimaryKeyRelatedField(queryset = TypeActivity.objects.all(), allow_null=True)
    company         = serializers.PrimaryKeyRelatedField(queryset = Company.objects.all(), allow_null=True)
    campaign        = serializers.PrimaryKeyRelatedField(queryset = Campaign.objects.all(), allow_null=True)
    user            = serializers.PrimaryKeyRelatedField(queryset = CustomUser.objects.all(), allow_null=True)    

    class Meta:
        model   = Activity
        #fields  = '__all__'
        exclude = ['created_at', 'update_at', 'status']
        read_only_fields    = ('activity_id', )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['type_activity'] = TypeActivitySerializer(instance.type_activity).data

        if instance.company is not None:
            representation['company'] = CompanySerializer(instance.company).data
        if instance.campaign is not None:
            representation['campaign'] = CampaignSerializer(instance.campaign).data
        if instance.user is not None:
            representation['user'] = UserSerializer(instance.user).data

        return representation