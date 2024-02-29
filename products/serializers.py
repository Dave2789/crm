from rest_framework import serializers
from .models import Price, Discount, DiscountScale, Product
from catalogs.models import Currency, ProductCategory, Country
from catalogs.serializers import CurrencySerializer, ProductCategorySerializer, CountrySerializer

class PriceSerializer(serializers.ModelSerializer):
    product_category    = serializers.PrimaryKeyRelatedField(queryset = ProductCategory.objects.all(), allow_null=True)
    currency   = serializers.PrimaryKeyRelatedField(queryset = Currency.objects.all(), allow_null=True)

    class Meta:
        model   = Price
        #fields  = '__all__'
        exclude = ['created_at', 'update_at', 'status']
        read_only_fields    = ('price_id', )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['product_category'] = None
        data['currency'] = None

        if instance.product_category is not None:
            data['product_category'] = ProductCategorySerializer(instance.product_category).data
        if instance.price is not None:
            data['currency'] = CurrencySerializer(instance.currency).data

        return data

class DiscountScaleSerializer(serializers.ModelSerializer):
    class Meta:
        model   = DiscountScale
        #fields  = '__all__'
        exclude = ['created_at', 'update_at', 'status', 'discount']
        read_only_fields    = ('discount_scale_id', )

class DiscountSerializer(serializers.ModelSerializer):
    discount_scales   = DiscountScaleSerializer(many=True, read_only=True)
    class Meta:
        model   = Discount
        #fields  = '__all__'
        exclude = ['created_at', 'update_at', 'status']
        read_only_fields    = ('discount_id', )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        discount_scales = instance.discountscale_set.all()
        representation['discount_scales'] = DiscountScaleSerializer(discount_scales, many=True).data
        return representation

class ProductSerializer(serializers.ModelSerializer):
    price       = serializers.PrimaryKeyRelatedField(queryset = Price.objects.all(), allow_null=True)
    discount    = serializers.PrimaryKeyRelatedField(queryset = Discount.objects.all(), allow_null=True)
    product_category    = serializers.PrimaryKeyRelatedField(queryset = ProductCategory.objects.all(), allow_null=True)
    country    = serializers.PrimaryKeyRelatedField(queryset = Country.objects.all(), allow_null=True)

    class Meta:
        model   = Product
        #fields  = '__all__'
        exclude = ['created_at', 'update_at', 'status']
        read_only_fields    = ('product_id', )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['price'] = None
        data['discount'] = None
        data['product_category'] = None
        data['country'] = None

        if instance.price is not None:
            data['price'] = PriceSerializer(instance.price).data
        if instance.discount is not None:
            data['discount'] = DiscountScaleSerializer(instance.discount).data
        if instance.product_category is not None:
            data['product_category'] = ProductCategorySerializer(instance.product_category).data
        if instance.country is not None:
            data['country'] = CountrySerializer(instance.country).data

        return data
    
class ProductInsertSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Product
        fields  = '__all__'
        read_only_fields    = ('product_id', )