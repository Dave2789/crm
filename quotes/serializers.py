from rest_framework import serializers
from .models import Quote, QuoteOption, OptionProduct
from products.serializers import ProductSerializer
from products.models import Product
from catalogs.models import Status, PaymentMethod
from catalogs.serializers import StatusSerializer, PaymentMethodSerializer
from companies.models import Company, CompanyContact
from companies.serializers import CompanySerializer, CompanyContactSerializer
from campaigns.models import Campaign
from campaigns.serializers import CampaignSerializer
from users.models import CustomUser
from users.serializers import UserSerializer

class OptionProductSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset = Product.objects.all(), allow_null=True)

    class Meta:
        model   = OptionProduct
        exclude = ['created_at', 'update_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['product']   = ProductSerializer(instance.product).data

        return representation
    
class OptionProductInsert(serializers.ModelSerializer):
    class Meta:
        model   = OptionProduct
        fields  = '__all__'
        read_only_fields    = ('option_product_id', )

class QuoteOptionSerializer(serializers.ModelSerializer):
    option_products = OptionProductSerializer(many=True, read_only=True)

    class Meta:
        model = QuoteOption
        exclude = ['created_at', 'update_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        option_products = instance.optionproduct_set.all()
        representation['option_products'] = OptionProductSerializer(option_products, many=True).data
        return representation
    
class QuoteOptionInsertSerializer(serializers.ModelSerializer):
    class Meta:
        model   = QuoteOption
        fields  = '__all__'
        read_only_fields    = ('quote_option_id', )

class QuoteSerializer(serializers.ModelSerializer):
    quote_options   = QuoteOptionSerializer(many=True, read_only=True)
    company         = serializers.PrimaryKeyRelatedField(queryset = Company.objects.all(), allow_null=True)
    contact         = serializers.PrimaryKeyRelatedField(queryset = CompanyContact.objects.all(), allow_null=True)
    user            = serializers.PrimaryKeyRelatedField(queryset = CustomUser.objects.all(), allow_null=True)
    campaign        = serializers.PrimaryKeyRelatedField(queryset = Campaign.objects.all(), allow_null=True)
    payment_method  = serializers.PrimaryKeyRelatedField(queryset = PaymentMethod.objects.all(), allow_null=True)
    status          = serializers.PrimaryKeyRelatedField(queryset = Status.objects.all(), allow_null=True)
    invoice_status  = serializers.PrimaryKeyRelatedField(queryset = Status.objects.all(), allow_null=True)
    
    
    class Meta:
        model   = Quote
        exclude = ['created_at', 'update_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        quote_options = instance.quoteoption_set.all()
        representation['quote_options'] = QuoteOptionSerializer(quote_options, many=True).data

        if instance.company is not None:
            representation['company'] = CompanySerializer(instance.company).data
        if instance.contact is not None:
            representation['contact'] = CompanyContactSerializer(instance.contact).data
        if instance.user is not None:
            representation['user'] = UserSerializer(instance.user).data
        if instance.campaign is not None:
            representation['campaign'] = CampaignSerializer(instance.campaign).data
        if instance.payment_method is not None:
            representation['payment_method'] = PaymentMethodSerializer(instance.payment_method).data
        if instance.status is not None:
            representation['status'] = StatusSerializer(instance.status).data
        if instance.invoice_status is not None:
            representation['invoice_status'] = StatusSerializer(instance.invoice_status).data

        return representation

class QuoteInsertSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Quote
        fields  = '__all__'
        read_only_fields    = ('quote_id', )