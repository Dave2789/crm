from datetime import date
from datetime import datetime
from activity.models import Activity
from campaigns.models import Campaign
from catalogs.models import CompanyPhase, InvoiceUse, PaymentCondition, PaymentMethod, WayToPay
from catalogs.utils import STATUS_COTIZACION_ACEPTADA, STATUS_COTIZACION_APROBADA, STATUS_COTIZACION_APROBADA_PC, STATUS_COTIZACION_CREADA, STATUS_COTIZACION_RECHAZA_CLIENTE, STATUS_COTIZACION_RECHAZA_LEAD, STATUS_ELIMINADO_DEFAULT, STATUS_FACTURADA, STATUS_PENDIENTE_FACTURAR, TYPE_ACTIVITY_NOTA, UUID_CLIENTE, UUID_LEAD, UUID_PROSPECTO, get_status_instance, get_type_activity_instance
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework import generics
from drf_yasg import openapi
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.db import transaction
from users.models import CustomUser
from .models import Quote, QuoteOption, OptionProduct
from .serializers import OptionProductInsert, QuoteInsertSerializer, QuoteOptionInsertSerializer, QuoteSerializer, QuoteOptionSerializer, OptionProductSerializer
from companies.models import Company, CompanyContact
from companies.serializers import CompanyContactSerializer, CompanySerializer
import facturama

class QuoteListCreateView(generics.ListCreateAPIView):
    queryset    = Quote.objects.all()
    serializer_class    = QuoteSerializer

    def get(self, request, *args, **kwargs):
        quotes = Quote.objects.all()
        serializer = QuoteSerializer(quotes, many=True)
        return Response(serializer.data)
    
    #CREATE FUNCTION --
    def create(self, request, *args, **kwargs):
        data = request.data
        company_data = data.get('company', None)
        company_id = company_data
        quote_data = data
        invoice_status  = get_status_instance(STATUS_PENDIENTE_FACTURAR)
        status_instance = get_status_instance(STATUS_COTIZACION_CREADA)

        try:
            with transaction.atomic():

                if company_id:
                    company = Company.objects.get(pk=company_id)
                    #VALIDAMOS LA FASE DE LA EMPRESA PARA ACTUALIZAR, SI ES PROSPECTO CAMBIA A LEAD, SI ES LEAD CAMBIA A CLIENTE, SI ES CLIENTE AHÍ SE QUEDA
                    if company.company_phase == UUID_PROSPECTO:
                        company.company_phase = UUID_LEAD
                    elif company.company_phase == UUID_LEAD:
                        company.company_phase = UUID_CLIENTE
                    
                    #CONSIDERAR ACTUALIZAR DATOS DE INDICADORES DE COTIZACIONES, ETC.
                    company.amout_quotes += 1 #CONTABILIZAR COTIZACIONES
                    company.save()

                else:
                    company_serializer = CompanySerializer(data=company_data)
                    if company_serializer.is_valid():
                        company = company_serializer.save()
                        #INICIAMOS LA CONTABILIZACION DE COTIZACIONES EN ESTA EMPRESA
                        company.amout_quotes = 1
                        company.save()

                        company_contact_serializer = CompanyContactSerializer(data=company_data)
                        if company_contact_serializer.is_valid():
                            company_contact = company_contact_serializer.save()
                        else:
                            return Response(company_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                        
                    else:
                        return Response(company_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
                quote_serializer = QuoteInsertSerializer(data = quote_data)
                if quote_serializer.is_valid():
                    #OBTENEMOS ESTATUS INICIAL DE LA COTIZACION
                    quote = quote_serializer.save(company=company, status = status_instance, invoice_status = invoice_status)
                else:
                    return Response(quote_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                quote_options_data = quote_data.get( 'quote_options', {} )

                for quote_option_data in quote_options_data:
                    quote_option_serializer = QuoteOptionInsertSerializer(data=quote_option_data)
                    if quote_option_serializer.is_valid():
                        quote_option = quote_option_serializer.save(quote = quote)
                        option_products_data = quote_option_data.get( 'option_products', {} )
                        for option_product_data in option_products_data:
                            option_product_serializer = OptionProductInsert(data=option_product_data)
                            if option_product_serializer.is_valid():
                                option_product_serializer.save(quote_option = quote_option)
                            else:
                                raise ValidationError(option_product_serializer.errors)
                    else:
                        raise ValidationError(quote_option_serializer.errors)

                #GUARDAR ACTIVIDAD DE CREACION
                user_id = data.get('user', None)
                campaign_id = data.get('campaign', None)
                user = CustomUser.objects.get(pk=user_id)
                campaign = Campaign.objects.get(pk=campaign_id)
                type_ctivity = get_type_activity_instance(TYPE_ACTIVITY_NOTA)
                quote_number = quote.quote_number
                Activity.objects.create(
                    company = company,
                    user    =   user,
                    type_activity   = type_ctivity,
                    campaign    = campaign,
                    description = f"Creación de Cotización con folio: {quote_number}.",
                    activity_date   = date.today(),
                    activity_hour   = datetime.now().time(),
                    end_date    = date.today(),
                    finish      = True,
                    process     = "Cotizaciones",
                    status      = status_instance
                )

        except ValidationError as e:
            return Response({'detail': 'Error de validación: ' + str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'detail': 'Error interno del servidor: ' + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(QuoteSerializer(quote).data, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        data = request.data
        quote_id = data.get('quote_id', None)

        if quote_id is None:
            return Response({"message": "Es necesario enviar el número de cotización"}, status=status.HTTP_204_NO_CONTENT)

        try:
            quote = Quote.objects.get(pk=quote_id)
        except Quote.DoesNotExist:
            return Response({"message": "Es necesario enviar el número de cotización valida"}, status=status.HTTP_204_NO_CONTENT)

        # Inicio de la transacción atómica
        with transaction.atomic():
            try:
                # Actualizamos los campos de la cotización según la solicitud
                quote_serializer = QuoteInsertSerializer(instance=quote, data=data)
                if quote_serializer.is_valid():
                    quote = quote_serializer.save()
                else:
                    return Response(quote_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                # Actualizamos las opciones de cotización
                quote_options_data = data.get('quote_options', [])
                for quote_option_data in quote_options_data:
                    quote_option_id = quote_option_data.get('quote_option_id')
                    try:
                        quote_option = QuoteOption.objects.get(pk=quote_option_id)
                    except QuoteOption.DoesNotExist:
                        continue  # La opción de cotización no existe, seguir con la siguiente
                    quote_option_serializer = QuoteOptionSerializer(instance=quote_option, data=quote_option_data)
                    if quote_option_serializer.is_valid():
                        quote_option = quote_option_serializer.save()
                    else:
                        raise ValidationError(quote_option_serializer.errors)

                    # Actualizamos los productos de opción
                    option_products_data = quote_option_data.get('option_products', [])
                    for option_product_data in option_products_data:
                        option_product_id = option_product_data.get('option_product_id')
                        try:
                            option_product = OptionProduct.objects.get(pk=option_product_id)
                        except OptionProduct.DoesNotExist:
                            continue  # El producto de opción no existe, seguir con el siguiente
                        option_product_serializer = OptionProductSerializer(instance=option_product, data=option_product_data)
                        if option_product_serializer.is_valid():
                            option_product = option_product_serializer.save()
                        else:
                            raise ValidationError(option_product_serializer.errors)

                # Comprobamos las opciones de cotización existentes y cambiamos su estado a "ELIMINADA" si no se proporcionan en la solicitud
                existing_quote_options_ids = [quote_option_data.get('quote_option_id') for quote_option_data in quote_options_data]
                quote.quote_options.exclude(pk__in=existing_quote_options_ids).update(status=get_status_instance(STATUS_ELIMINADO_DEFAULT))

                # Comprobamos los productos de opción existentes y cambiamos su estado a "ELIMINADA" si no se proporcionan en la solicitud
                existing_option_products_ids = [option_product_data.get('option_product_id') for quote_option_data in quote_options_data for option_product_data in quote_option_data.get('option_products', [])]
                OptionProduct.objects.filter(quote_option__quote=quote, status=get_status_instance(STATUS_ELIMINADO_DEFAULT)).exclude(pk__in=existing_option_products_ids).update(status=get_status_instance(STATUS_ELIMINADO_DEFAULT))

                # Guardamos la actividad de actualización
                user_id = data.get('user', None)
                campaign_id = data.get('campaign', None)
                user = CustomUser.objects.get(pk=user_id)
                campaign = Campaign.objects.get(pk=campaign_id)
                type_ctivity = get_type_activity_instance(TYPE_ACTIVITY_NOTA)
                quote_number = quote.quote_number
                Activity.objects.create(
                    company=quote.company,
                    user=user,
                    type_activity=type_ctivity,
                    campaign=campaign,
                    description=f"Actualización de Cotización con folio: {quote_number}.",
                    activity_date=date.today(),
                    activity_hour=datetime.now().time(),
                    end_date=date.today(),
                    finish=True,
                    process="Cotizaciones",
                    status=quote.status
                )

                # Commit de la transacción
                transaction.commit()

            except ValidationError as e:
                transaction.rollback()
                return Response({'detail': 'Error de validación: ' + str(e)}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                transaction.rollback()
                return Response({'detail': 'Error interno del servidor: ' + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(QuoteSerializer(quote).data, status=status.HTTP_200_OK)

class QuoteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset    = Quote.objects.all()
    serializer_class    = QuoteSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        status_instance_deleted = get_status_instance(STATUS_ELIMINADO_DEFAULT)
        instance.status = status_instance_deleted
        instance.save()

        return Response({"message": "La cotización se ha eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)

class QuoteOptionListCreateView(generics.ListCreateAPIView):
    queryset    = QuoteOption.objects.all()
    serializer_class    = QuoteOptionSerializer

class QuoteOptionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset    = QuoteOption.objects.all()
    serializer_class    = QuoteOptionSerializer

class OptionProductListCreateView(generics.ListCreateAPIView):
    queryset    = OptionProduct.objects.all()
    serializer_class    = OptionProductSerializer

class OptionProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset    = OptionProduct.objects.all()
    serializer_class    = OptionProductSerializer

class QuoteTracking(APIView):
    def post(self, request):
        data = request.data
        quote_data = data.get('quote', {})
        quote_id    = quote_data.get('quote_id', None)
        status_id   = quote_data.get('status_id', None)
        company_id  = quote_data.get('company_id', None)
        #Validamos que se esten recibiendo los datos necesarios
        if quote_id is None:
            return Response({"message": "Es necesario enviar el número de cotización"}, status=status.HTTP_204_NO_CONTENT)
        
        if status_id is None:
            return Response({"message": "Es necesario enviar el estatus de cotización"}, status=status.HTTP_204_NO_CONTENT)
        
        #VAMOS POR LA INSTANCIA DE LA COTIZACION
        quote_instance = Quote.objects.get(pk = quote_id)
        #VAMOS POR LA INSTANCIA DEL ESTATUS
        status_instance = get_status_instance(status_id)
        #VAMOS POR LA INSTANCIA DE LA EMPRESA
        company_instance = Company.objects.get(pk = company_id)

        if status_id == STATUS_COTIZACION_ACEPTADA:
            #CAMBIAR ESTATUS DE LA EMPRESA DE LEAD A CLIENTE
            company_phase = CompanyPhase.objects.get(pk=UUID_CLIENTE)
            company_instance.company_phase = company_phase
            company_instance.save()
        elif status_id == STATUS_COTIZACION_APROBADA:
            #MARCAMOS LA OPCION DE COTIZACION QUE ELIGIÓ
            quote_option_id = quote_data.get( 'quote_option_id', None )
            quote_option_instance = QuoteOption.objects.get(pk = quote_option_id)
            quote_option_instance.selected = True
            quote_option_instance.save()
            #VERIFICAMOS/ACTUALIZAMOS LOS DATOS DE FACTURACIÓN
            payment_method = PaymentMethod.objects.get(pk = quote_data.get('payment_method_id', None))
            way_to_pay     = WayToPay.objects.get(pk = quote_data.get('way_to_pay_id', None))
            payment_condition   = PaymentCondition.objects.get(pk = quote_data.get('payment_condition_id', None))
            invoice_use = InvoiceUse.objects.get(pk = quote_data.get('invoice_use_id', None))
            company_instance.payment_method     = payment_method
            company_instance.way_to_pay         = way_to_pay
            company_instance.payment_condition  = payment_condition
            company_instance.invoice_use        = invoice_use
            company_instance.save()
        elif status_id == STATUS_COTIZACION_APROBADA_PC:
            #DINERO EN CUENTA ACTUALIZAMOS EL VALOR
            quote_instance.money_in_account     = True
            quote_instance.payment_date         = date.today()
        
        #ACTUALIZAMOS EL ESTATUS DE LA COTIZACION
        quote_instance.status = status_instance
        quote_instance.save()

        return Response({"message": "Operación realizada con éxito"}, status=status.HTTP_200_OK)

class QuoteInvoice(APIView):
    def post(self, request):
        data = request.data
        quote_data = data.get('quote', {})
        quote_id    = quote_data.get('quote_id', None)
        status_id   = quote_data.get('status_id', None)
        invoice_status_id  = quote_data.get('invoice_status_id', None)

        #Validamos que se esten recibiendo los datos necesarios
        if quote_id is None:
            return Response({"message": "Es necesario enviar el número de cotización"}, status=status.HTTP_204_NO_CONTENT)
        
        if status_id is None:
            return Response({"message": "Es necesario enviar el estatus de cotización"}, status=status.HTTP_204_NO_CONTENT)
        
        #VAMOS POR LA INSTANCIA DE LA COTIZACION
        quote_instance = Quote.objects.get(pk = quote_data.get('quote_id', None))
        #VAMOS POR LA INSTANCIA DEL ESTATUS
        status_instance = get_status_instance(status_id)
        #VAMOS POR LA INSTANCIA DE LA EMPRESA
        company_instance = Company.objects.get(pk = quote_data.get('company_id', None))
        #VAMOS POR LA INSTANCIA DEL ESTATUS DE FACTURACION
        status_invoice_instance = get_status_instance(invoice_status_id)
        cfdi = True

        '''if invoice_status_id == STATUS_FACTURADA:
            #FACTURAMOS CON API
            facturama.sandbox = True
            facturama._credentials = ('DavidLuna', 'JYUb@#Za')

            cfdi4_object = {
                    "Folio": "100",
                    "ExpeditionPlace": "78140",
                    "PaymentConditions": "CREDITO A SIETE DIAS",
                    "CfdiType": "I",
                    "PaymentForm": "03",
                    "PaymentMethod": "PUE",
                    "Receiver": {
                        "Rfc": "EKU9003173C9",
                        "Name": "ESCUELA KEMPER URGATE",
                        "CfdiUse": "G03",
                        "FiscalRegime": "603",
                        "TaxZipCode": "26015"
                    },
                    "Items": [
                        {
                            "ProductCode": "10101504",
                            "IdentificationNumber": "EDL",
                            "Description": "Estudios de viabilidad",
                            "Unit": "NO APLICA",
                            "UnitCode": "MTS",
                            "UnitPrice": 50.0,
                            "Quantity": 2.0,
                            "Subtotal": 100.0,
                            "TaxObject": "02",
                            "Taxes": [
                                {
                                    "Total": 16.0,
                                    "Name": "IVA",
                                    "Base": 100.0,
                                    "Rate": 0.16,
                                    "IsRetention": False
                                }
                            ],
                            "Total": 116.0
                        }
                    ]
            }

            try:
                #cfdi = facturama.Cfdi.create3(cfdi4_object)
                cfdi = facturama.Cfdi.create3(cfdi4_object)
                facturama.Cfdi.send_by_email('issued','GgQKVvV84IlgmFCMqJVraQ2','davidlunaperez27@gmail.com')
            except Exception as e:
                return Response({'mensaje': f'Error al crear la factura: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)'''

        
        quote_instance.status           = status_instance
        quote_instance.invoice_status   = status_invoice_instance
        quote_instance.save()

        if cfdi:
            return Response({'mensaje': 'Factura generada correctamente'}, status=status.HTTP_200_OK)
        else:
            return Response({'mensaje': 'Error al generar la factura'}, status=500)