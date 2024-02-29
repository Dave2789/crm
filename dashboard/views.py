from catalogs.utils import STATUS_COTIZACION_APROBADA_PC, STATUS_COTIZACION_CREADA, STATUS_COTIZACION_RECHAZA_CLIENTE, STATUS_COTIZACION_RECHAZA_LEAD, UUID_CLIENTE, UUID_LEAD
from companies.models import Company
from quotes.models import Quote
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.db.models import Sum

@api_view(['GET'])
def dashboard_statics(request):
    #OBTENEMOS COTIZACIONES DE LEADS - PARA SABER QUE COTIZACIONES HAY DE LEADS OBTENGO LAS EMPRESAS EN ESA FASE
    companies_leads     = Company.objects.filter(company_phase = UUID_LEAD)
    company_lead_ids    = companies_leads.values_list('company_id', flat=True)
    lead_quotes_creadas = Quote.objects.filter(company_id__in = company_lead_ids, status = STATUS_COTIZACION_CREADA)
    lead_quotes_rechazadas  = Quote.objects.filter(company_id__in = company_lead_ids, status = STATUS_COTIZACION_RECHAZA_LEAD)
    total_lead_quotes_creadas   = lead_quotes_creadas.count()
    total_lead_quotes_rechazadas    = lead_quotes_rechazadas.count()
    total_lead_quotes_amount    = lead_quotes_creadas.aggregate(Sum('quote_total'))['quote_total__sum'] or 0
    total_lead_quotes_amount_rechazadas = lead_quotes_rechazadas.aggregate(Sum('quote_total'))['quote_total__sum'] or 0
    #OBTENEMOS COTIZACIONES DE CLIENTES - PARA SABER QUE COTIZACIONES HAY DE CLIENTES OBTENGO LAS EMPRESAS EN ESA FASE
    companies_clients   = Company.objects.filter(company_phase = UUID_CLIENTE)
    company_client_ids  = companies_clients.values_list('company_id', flat=True)
    client_quotes_creadas   = Quote.objects.filter(company_id__in = company_client_ids, status = STATUS_COTIZACION_CREADA)
    client_quotes_rechazadas    = Quote.objects.filter(company_id__in = company_client_ids, status = STATUS_COTIZACION_RECHAZA_CLIENTE)
    total_client_quotes_creadas = client_quotes_creadas.count()
    total_client_quotes_rechazadas  = client_quotes_rechazadas.count()
    total_client_quotes_amount  = client_quotes_creadas.aggregate(Sum('quote_total'))['quote_total__sum'] or 0
    total_client_quotes_amount_rechazadas  = client_quotes_rechazadas.aggregate(Sum('quote_total'))['quote_total__sum'] or 0

    client_quotes_approved = Quote.objects.filter(company_id__in=company_client_ids, status=STATUS_COTIZACION_APROBADA_PC)
    total_client_quotes_approved = client_quotes_approved.count()
    total_client_quotes_amount_approved = client_quotes_approved.aggregate(Sum('quote_total'))['quote_total__sum'] or 0

    response_data = {
        'total_lead_quotes_creadas'         : total_lead_quotes_creadas,
        'total_lead_quotes_amount_creadas'  : total_lead_quotes_amount,
        'total_client_quotes_creadas'       : total_client_quotes_creadas,
        'total_client_quotes_amount_creadas': total_client_quotes_amount,
        'total_lead_quotes_rechazadas'      : total_lead_quotes_rechazadas,
        'total_client_quotes_rechazadas'    : total_client_quotes_rechazadas,
        'total_lead_quotes_amount_rechazadas'   :   total_lead_quotes_amount_rechazadas,
        'total_client_quotes_amount_rechazadas' :   total_client_quotes_amount_rechazadas,
        'total_client_quotes_approved'       : total_client_quotes_approved,
        'total_client_quotes_amount_approved': total_client_quotes_amount_approved,
    }

    return Response(response_data, status=status.HTTP_200_OK)

@api_view(['GET'])
def dashboard_graphics(request):
    
    return Response({'mensaje': 'Dashboard Gráficas'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def dashboard_products(request):

    return Response({'mensaje': 'Dashboard Productos'}, status=status.HTTP_200_OK)