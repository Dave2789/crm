import uuid
from django.db import models
from users.models import CustomUser
from companies.models import Company
from catalogs.models import Status, CampaignType
from products.models import ProductCategory

class Campaign(models.Model):
    campaign_id             = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, help_text="UUID campaña")
    campaign_code           = models.CharField(max_length = 50, default = '', help_text="Codigo de campaña")
    campaign_name           = models.CharField(max_length = 150, default = '', help_text="Nombre de campaña")
    amount_invested         = models.DecimalField(max_digits = 10, default=0, decimal_places = 4, blank = True, help_text="Monto invertido")
    campaign_type           = models.ForeignKey(CampaignType, on_delete = models.CASCADE, blank = True, null = True, default = None, help_text="UUID Tipo de campaña")
    owner_user              = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank = True, null = True, default = None, help_text="UUID Agente/Usuario encargado/principal")
    start_date              = models.DateField(blank = True, help_text="Fecha de inicio")
    end_date                = models.DateField(blank = True, help_text="Fecha de termino")
    product_category        = models.ForeignKey(ProductCategory, on_delete = models.CASCADE, blank = True, null = True, default = None, help_text="UUID Categoria Producto / Solucion") #Solution
    description             = models.TextField(default = '', help_text="Descripcion")
    goal_total_companies    = models.IntegerField(default = 0, help_text="Meta Total de empresas a alcanzar")
    goal_total_responses    = models.IntegerField(default = 0, help_text="Meta Cantidad de respuestas")
    goal_number_quotes      = models.IntegerField(default = 0, help_text="Meta Cantidad cotizaciones")
    goal_number_sales       = models.IntegerField(default = 0, help_text="Meta Cantidad de cierres de venta")
    goal_amount             = models.DecimalField(max_digits = 10, default=0, decimal_places = 4, blank = True, help_text="Meta Monto total $")
    total_companies         = models.IntegerField( default = 0, help_text="Total empresas alcanzadas")
    number_quotes_lead      = models.IntegerField(default = 0, help_text="Cantidad Total cotizaciones Lead")
    number_quotes_client    = models.IntegerField(default = 0, help_text="Cantidad Total cotizaciones Clientes")
    amout_quotes_lead       = models.DecimalField(max_digits = 10, default=0, decimal_places = 4, blank = True, help_text="Total cotizaciones Leads monto $")
    amout_quotes_client     = models.DecimalField(max_digits = 10, default=0, decimal_places = 4, blank = True, help_text="Total cotizaciones Clientes monto $")
    total_sales             = models.IntegerField(default = 0, help_text="Cantidad Total ventas cerradas")
    total_amount            = models.DecimalField(max_digits = 10, default=0, decimal_places = 4, blank = True, help_text="Total ventas cerradas monto $")
    average_quote           = models.DecimalField(max_digits = 10, default=0, decimal_places = 4, blank = True, help_text="Costo promedio por cotizacion monto $")
    average_sales           = models.DecimalField(max_digits = 10, default=0, decimal_places = 4, blank = True, help_text="Costo promedio por venta monto $")
    status                  = models.ForeignKey(Status, on_delete = models.CASCADE, blank = True, null = True, default = None, help_text="UUID Estatus")
    register_date           = models.DateField(blank=True, null=True, help_text="Fecha de registro Front")
    created_at              = models.DateTimeField(auto_now_add = True, help_text="Fecha de creacion interna sistema")
    update_at               = models.DateTimeField(auto_now = True, help_text="Fecha de actualizacion interna sistema")

class CampaignUser(models.Model):
    campaign_user_id    = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, help_text="UUID Campaign-User")
    campaign            = models.ForeignKey(Campaign, related_name='users', on_delete = models.CASCADE, null = True, blank = True, default = None, help_text="UUID Campaign relacionada")
    user                = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank = True, null=True, default = None, help_text="UUID Usuario/Agente relacionado")
    status      = models.ForeignKey(Status, on_delete = models.CASCADE, blank = True, null = True, default = None, help_text="UUID Estatus")
    created_at  = models.DateTimeField(auto_now_add = True, help_text="Fecha de creacion interna sistema")
    update_at   = models.DateTimeField(auto_now = True, help_text="Fecha de actualizacion interna sistema")

class CampaignCompany(models.Model):
    campaign_company_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, help_text="UUID Campaign-Company")
    campaign    = models.ForeignKey(Campaign, related_name='companies', on_delete = models.CASCADE, null = True, blank = True, default = None, help_text="UUID Campaign relacionada")
    company     = models.ForeignKey(Company, on_delete=models.CASCADE, blank = True, null = True, default = None, help_text="UUID Company relacionada")
    total_quote = models.DecimalField(max_digits = 10, default=0, decimal_places = 4, blank = True, help_text="Monto total cotizado $")
    total_sale  = models.DecimalField(max_digits = 10, default=0, decimal_places = 4, blank = True, help_text="Monto total vendido $")
    response    = models.BooleanField(default = False, help_text="Respuesta de la empresa")
    status      = models.ForeignKey(Status, on_delete = models.CASCADE, blank = True, default = None, null = True, help_text="UUID Estatus")
    created_at  = models.DateTimeField(auto_now_add = True, help_text="Fecha de creacion interna sistema")
    update_at   = models.DateTimeField(auto_now = True, help_text="Fecha de actualizacion interna sistema")