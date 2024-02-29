import uuid
from django.db import models

class Status(models.Model):
    status_id   = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, help_text="UUID Estatus")
    description = models.TextField(max_length = 100, default = '', help_text="Descripcion/Nombre del Estatus")
    module      = models.IntegerField(default = 1, help_text="Modulo/Submodulo al cual pertenece el Estatus 1. Sistema, 2. Campaing, 3. Company, 4. Products, 5. Quote, 6. Facturacion")
    created_at  = models.DateTimeField(auto_now_add = True)
    update_at   = models.DateTimeField(auto_now = True)

class Country(models.Model):
    country_id      = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, help_text="UUID Pais")
    country_name    = models.CharField(max_length = 100, default = '', help_text="Nombre pais")
    status          = models.ForeignKey(Status, on_delete = models.CASCADE, blank = True, null = True, default = None, help_text="UUID Estatus")
    created_at      = models.DateTimeField(auto_now_add = True)
    update_at       = models.DateTimeField(auto_now = True)

class State(models.Model):
    state_id    = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, help_text="UUID Estado")
    country     = models.ForeignKey(Country, on_delete = models.CASCADE, blank = True, default = None, null = True, help_text="UUID Pais")
    state_name  = models.CharField(max_length = 100, default = '', help_text="Nombre del estado")
    status      = models.ForeignKey(Status, on_delete = models.CASCADE, blank = True, null = True, default = None, help_text="UUID Estatus")
    created_at  = models.DateTimeField(auto_now_add = True)
    update_at   = models.DateTimeField(auto_now = True)

class City(models.Model):
    city_id     = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, help_text="UUID Ciudad")
    state       = models.ForeignKey(State, on_delete = models.CASCADE, blank = True, default = None, null = True, help_text="UUID Estado")
    city_name   = models.CharField(max_length = 100, default = '', help_text="Nombre de la ciudad")
    status      = models.ForeignKey(Status, on_delete = models.CASCADE, blank = True, null = True, default = None, help_text="UUID Estatus")
    created_at  = models.DateTimeField(auto_now_add = True)
    update_at   = models.DateTimeField(auto_now = True)

class Business(models.Model):
    business_id     = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, help_text="UUID Giro de empresa")
    business_name   = models.CharField(max_length = 100, default = '', help_text="Descripcion / Nombre de Giro")
    status      = models.ForeignKey(Status, on_delete = models.CASCADE, blank = True, default = None, null = True, help_text="UUID Estatus")
    created_at  = models.DateTimeField(auto_now_add = True)
    update_at   = models.DateTimeField(auto_now = True)

class Platform(models.Model):
    platform_id     = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, help_text="UUID Plataforma. ej. Abrevius Capacitacion")
    platform_name   = models.CharField(max_length = 100, default = '', help_text="Nombre de la plataforma/solucion")
    status      = models.ForeignKey(Status, on_delete = models.CASCADE, blank = True, default = None, null = True, help_text="UUID Estatus")
    created_at  = models.DateTimeField(auto_now_add = True)
    update_at   = models.DateTimeField(auto_now = True)

class Rol(models.Model):
    rol_id     = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, help_text="UUID Rol")
    rol_name   = models.CharField(max_length = 100, default = '', help_text="Nombre del rol")
    permissions = models.JSONField(default = dict, blank = True, null = True, help_text="Permisos default")
    status      = models.ForeignKey(Status, on_delete = models.CASCADE, blank = True, null = True, default = None, help_text="UUID Estatus")
    created_at  = models.DateTimeField(auto_now_add = True)
    update_at   = models.DateTimeField(auto_now = True)

class PaymentMethod(models.Model):
    payment_method_id   = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, help_text="UUID Metodo de pago")
    payment_name    = models.CharField(max_length = 100, default = '', help_text="Nombre del metodo de pago")
    status      = models.ForeignKey(Status, on_delete = models.CASCADE, blank = True, null = True, default = None, help_text="UUID Estatus")
    created_at  = models.DateTimeField(auto_now_add = True)
    update_at   = models.DateTimeField(auto_now = True)

class CompanyType(models.Model):
    company_type_id     = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, help_text="UUID Tipo de empresa")
    type_name   = models.CharField(max_length = 100, default = '', help_text="Tipo de empresa, ej. Partner, Individual, Empresa")
    status      = models.ForeignKey(Status, on_delete = models.CASCADE, blank = True, null = True, default = None, help_text="UUID Estatus")
    created_at  = models.DateTimeField(auto_now_add = True)
    update_at   = models.DateTimeField(auto_now = True)

class CompanySize(models.Model):
    company_size_id     = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, help_text="UUID Tamanio de empresa")
    size_name   = models.CharField(max_length = 100, default = '', help_text="Nombre tamanio empresa")
    status      = models.ForeignKey(Status, on_delete = models.CASCADE, blank = True, null = True, default = None, help_text="UUID Estatus")
    created_at  = models.DateTimeField(auto_now_add = True)
    update_at   = models.DateTimeField(auto_now = True)

class CompanyPhase(models.Model):
    company_phase_id    = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, help_text="UUID Fase de la empresa")
    phase_name  = models.CharField(max_length = 100, default = '', help_text="Nombre de la fase, ej. Prospecto, Lead, Cliente")
    status      = models.ForeignKey(Status, on_delete = models.CASCADE, blank = True, null = True, default = None, help_text="UUID Estatus")
    created_at  = models.DateTimeField(auto_now_add = True)
    update_at   = models.DateTimeField(auto_now = True)

class CampaignType(models.Model):
    campaign_type_id    = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, help_text="UUID Tipo de campaña")
    campaign_type_name  = models.CharField(max_length = 100, default = '', help_text="Nombre de tipo de campaña")
    status      = models.ForeignKey(Status, on_delete = models.CASCADE, blank = True, null = True, default = None, help_text="UUID Estatus")
    created_at  = models.DateTimeField(auto_now_add = True, help_text="Fecha creacion")
    update_at   = models.DateTimeField(auto_now = True, help_text="Fecha ultima actualizacion")

class ProductCategory(models.Model):
    product_category_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, help_text="UUID Categoria de producto")
    category_name   = models.CharField(max_length = 100, default = '', help_text="Nombre de categoria")
    description     = models.TextField(default = '', help_text="Descripcion de la categoria")
    status      = models.ForeignKey(Status, on_delete = models.CASCADE, blank = True, null = True, default = None, help_text="UUID Estatus")
    created_at  = models.DateTimeField(auto_now_add = True)
    update_at   = models.DateTimeField(auto_now = True)

class TypeActivity(models.Model):
    type_activity_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, help_text="UUID Tipo de Actividad")
    activity    = models.CharField(max_length = 100, default = '', help_text="Nombre de la actividad")
    icon        = models.CharField(max_length = 100, default = '', help_text="Icono")
    color       = models.CharField(max_length = 100, default = '', help_text="Color")
    status      = models.ForeignKey(Status, on_delete = models.CASCADE, blank = True, null = True, default = None, help_text="UUID Estatus")
    created_at  = models.DateTimeField(auto_now_add = True)
    update_at   = models.DateTimeField(auto_now = True)

class SubTypeActivity(models.Model):
    sub_type_activity_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, help_text="UUID Tipo de Sub actividad")
    type_activity   = models.ForeignKey(TypeActivity, on_delete = models.CASCADE, blank = True, null = True, default = None, help_text="UUID Actividad")
    sub_activity    = models.CharField(max_length = 100, default = '', help_text="Nombre de la sub actividad")
    color       = models.CharField(max_length = 100, default = '', help_text="Color")
    status      = models.ForeignKey(Status, on_delete = models.CASCADE, blank = True, null = True, default = None, help_text="UUID Estatus")
    created_at  = models.DateTimeField(auto_now_add = True)
    update_at   = models.DateTimeField(auto_now = True)

class Currency(models.Model):
    currency_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, help_text="UUID Moneda")
    currency_name = models.CharField(max_length = 100, default = '', help_text="Nombre de la moneda")
    currency_abrev  = models.CharField(max_length = 100, default = '', help_text="Abreviatura de la moneda")
    symbol      = models.CharField(max_length = 100, default = '', help_text="Abreviatura de la moneda")
    status      = models.ForeignKey(Status, on_delete = models.CASCADE, blank = True, null = True, default = None, help_text="UUID Estatus")
    created_at  = models.DateTimeField(auto_now_add = True)
    update_at   = models.DateTimeField(auto_now = True)

class WayToPay(models.Model):
    way_to_pay_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, help_text="UUID Forma de pago")
    way_to_pay_code = models.CharField(max_length = 100, default = '', help_text="Codigo de la forma")
    way_to_pay_name = models.CharField(max_length = 100, default = '', help_text="Nombre de la forma de pago")
    status      = models.ForeignKey(Status, on_delete = models.CASCADE, blank = True, null = True, default = None, help_text="UUID Estatus")
    created_at  = models.DateTimeField(auto_now_add = True)
    update_at   = models.DateTimeField(auto_now = True)

class PaymentCondition(models.Model):
    payment_condition_id   = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, help_text="UUID Condiciones de pago")
    payment_condition_name = models.CharField(max_length = 100, default = '', help_text="Nombre de la condicion de pago")
    status      = models.ForeignKey(Status, on_delete = models.CASCADE, blank = True, null = True, default = None, help_text="UUID Estatus")
    created_at  = models.DateTimeField(auto_now_add = True)
    update_at   = models.DateTimeField(auto_now = True)

class InvoiceUse(models.Model):
    invoice_use_id   = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, help_text="UUID Uso de CFDI")
    invoice_use_code = models.CharField(max_length = 100, default = '', help_text="Codigo del Uso")
    invoice_use_name = models.CharField(max_length = 100, default = '', help_text="Nombre del Uso")
    status      = models.ForeignKey(Status, on_delete = models.CASCADE, blank = True, null = True, default = None, help_text="UUID Estatus")
    created_at  = models.DateTimeField(auto_now_add = True)
    update_at   = models.DateTimeField(auto_now = True)