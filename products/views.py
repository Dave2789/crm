from catalogs.models import ProductCategory
from catalogs.utils import STATUS_ACTIVO_DEFAULT, get_status_instance
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from .models import Price, Discount, DiscountScale, Product
from .serializers import PriceSerializer, DiscountSerializer, DiscountScaleSerializer, ProductInsertSerializer, ProductSerializer
from django.shortcuts import get_object_or_404
from django.db import transaction

class PriceListCreateView(generics.ListCreateAPIView):
    queryset    = Price.objects.all()
    serializer_class    = PriceSerializer

    def create(self, request, *args, **kwargs):
        #OBTENEMOS EL ESTATUS POR DEFAULT
        status_instance = get_status_instance(STATUS_ACTIVO_DEFAULT)
        serializer = PriceSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        price_instance = serializer.save(status = status_instance)

        #OBTENEMOS TODOS LOS PRODUCTOS CON LA CATEGORIA ENVIADA
        product_category_id = request.data.get('product_category_id')

        if product_category_id:
            #OBTENEMOS INSTANCIA DE LA CATEGORIA
            product_category_instance = get_object_or_404(ProductCategory, product_category_id = product_category_id)
            products = Product.objects.filter(product_category = product_category_instance)

            for product in products:
                product.price = price_instance
                product.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class PriceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset    = Price.objects.all()
    serializer_class    = PriceSerializer

class DiscountListCreateView(generics.ListCreateAPIView):
    queryset    = Discount.objects.all()
    serializer_class    = DiscountSerializer

    def create(self, request, *args, **kwargs):
        #OBTENEMOS EL ESTATUS POR DEFAULT
        data = request.data
        discount_data = data.get('discount', {})
        discount_scales_data = discount_data.discount_scales

        try:
            with transaction.atomic():

                status_instance = get_status_instance(STATUS_ACTIVO_DEFAULT)
                serializer = ProductInsertSerializer(data = request.data)
                serializer.is_valid(raise_exception=True)
                discount = serializer.save(status = status_instance)

                for discount_scale in discount_scales_data:
                    discount_scale_serializer = DiscountScaleSerializer(data=discount_scale)
                    if discount_scale_serializer.is_valid():
                        discount_scale_option = discount_scale_serializer.save()
                        DiscountScale.objects.create(discount=discount, **discount_scale_option)

        except ValidationError as e:
            return Response({'detail': 'Error de validación: ' + str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'detail': 'Error interno del servidor: ' + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.data, status=status.HTTP_201_CREATED)        
        
class DiscountRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset    = Discount.objects.all()
    serializer_class    = DiscountSerializer

class DiscountScaleListCreateView(generics.ListCreateAPIView):
    queryset    = DiscountScale.objects.all()
    serializer_class    = DiscountScaleSerializer

class DiscountScaleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset    = DiscountScale.objects.all()
    serializer_class    = DiscountScaleSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset    = Product.objects.all()
    serializer_class    = ProductSerializer

    def create(self, request, *args, **kwargs):
        #OBTENEMOS EL ESTATUS POR DEFAULT
        status_instance = get_status_instance(STATUS_ACTIVO_DEFAULT)
        serializer = ProductInsertSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(status = status_instance)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset    = Product.objects.all()
    serializer_class    = ProductSerializer