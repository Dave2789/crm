import uuid
from django.db import models
from users.models import CustomUser
from django.utils.text import slugify
from catalogs.models import Country, InvoiceUse, PaymentCondition, PaymentMethod, State, City, Status, Business, Platform, CompanySize, CompanyType, CompanyPhase, WayToPay

class Company(models.Model):
    company_id      = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, help_text="UUID de la Empresa")
    company_name    = models.CharField(max_length = 150, default = '', help_text="Nombre de la empresa")
    slug            = models.SlugField(unique = True, null = True, blank = True, default = None, help_text="Slug de la empresa")
    tax_id_number   = models.CharField(max_length = 50, default = '', blank = True, null = True, help_text="numero de identificacion, ej. RFC")
    email           = models.EmailField(max_length = 150, blank = True, default = '', null = True, help_text="Email de la empresa")
    phone_number    = models.CharField(max_length = 50, default = '', help_text="Numero telefonico fijo de la empresa")
    web_page        = models.URLField(default = '', help_text="Web de la empresa")
    owner_user      = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank = True, related_name='owned_companies', default = '', null = True, help_text="Agente/Usuario propietario")
    country         = models.ForeignKey(Country, on_delete = models.CASCADE, blank = True, default = None, null = True, help_text="UUID Pais")
    state           = models.ForeignKey(State, on_delete = models.CASCADE, blank = True, default = None, null = True, help_text="UUID Estado")
    city            = models.ForeignKey(City, on_delete = models.CASCADE, blank = True, default = None, null = True, help_text="UUID Ciudad")
    address         = models.TextField(default = '', blank = True, null = True, help_text="Direccion de la empresa")
    business        = models.ForeignKey(Business, on_delete = models.CASCADE, blank = True, default = None, null = True, help_text="UUID Giro de la empresa")
    platform        = models.ForeignKey(Platform, on_delete = models.CASCADE, blank = True, default = None, null = True, help_text="UUID Plataforma que le interesa o proviene la empresa/Origen")
    company_size    = models.ForeignKey(CompanySize, on_delete = models.CASCADE, blank = True, default = None, null = True, help_text="UUID Tamanio de empresa")
    company_type    = models.ForeignKey(CompanyType, on_delete = models.CASCADE, blank = True, default = None, null = True, help_text="UUID Tipo de empresa")
    company_phase   = models.ForeignKey(CompanyPhase, on_delete = models.CASCADE, blank = True, default = None, null = True, help_text="UUID Fase de la empresa")
    logo            = models.ImageField(upload_to = 'logos/', blank = True, default = 'default.png', null = True, help_text="Logo")
    amout_quotes    = models.IntegerField(default = 0, blank = True, help_text="Total cotizaciones")
    amout_sales     = models.IntegerField(default = 0, blank = True, help_text="Total ventas")
    total_quotes    = models.DecimalField(max_digits = 10, decimal_places = 4, default = 0, blank = True, help_text="Monto total cotizaciones $")
    total_sales     = models.DecimalField(max_digits = 10, decimal_places = 4, default = 0, blank = True, help_text="Monto total ventas $")
    comments        = models.TextField(default = '', blank = True, null = True, help_text="Comentarios")
    payment_method  = models.ForeignKey(PaymentMethod, on_delete = models.CASCADE, blank = True, default = None, null = True, help_text="UUID Metodo de pago")
    way_to_pay      = models.ForeignKey(WayToPay, on_delete = models.CASCADE, blank = True, default = None, null = True, help_text="UUID Forma de pago")
    payment_condition   = models.ForeignKey(PaymentCondition, on_delete = models.CASCADE, blank = True, default = None, null = True, help_text="UUID Condiciones de pago")
    invoice_use     = models.ForeignKey(InvoiceUse, on_delete = models.CASCADE, blank = True, default = None, null = True, help_text="UUID Uso de CFDI")
    status          = models.ForeignKey(Status, on_delete = models.CASCADE, blank = True, default = None, null = True, help_text="UUID Estatus")
    register_user   = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank = True, default = None, related_name='registered_companies', null = True, help_text="UUID Usuario que registro")
    register_date   = models.DateField(blank=True, null=True, help_text="Fecha de registro Front")
    created_at  = models.DateTimeField(auto_now_add = True, help_text="Fecha de creacion interno de sistema")
    update_at   = models.DateTimeField(auto_now = True, help_text="Fecha de actualizacion")

    def save(self, *args, **kwargs):
        if not self.slug or not self.company_name:
            if self.company_name:
                base_slug = slugify(self.company_name)
            else:
                base_slug = 'company'

            slug = base_slug
            counter = 1
            while Company.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

class CompanyContact(models.Model):
    contact_id  = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, help_text="UUID Contacto-Empresa")
    company     = models.ForeignKey(Company, on_delete=models.CASCADE, blank = True, null = True, default = None, help_text="UUID Empresa relacionada")
    full_name   = models.CharField(max_length = 150, default = '', help_text="Nombre de la completo", blank = True, null = True)
    position    = models.CharField(max_length = 150, default = '', help_text="Puesto en la empresa", blank = True, null = True)
    email       = models.EmailField(max_length = 150, blank = True, default = '', help_text="email de contacto")
    movil_phone = models.CharField(default = '', help_text="Movil de contacto", blank = True, null = True)
    local_phone = models.CharField(default = '', help_text="Numero fijo de contacto", blank = True, null = True)
    ext         = models.CharField(default = '', help_text="Extension", blank = True, null = True)
    status      = models.ForeignKey(Status, on_delete = models.CASCADE, blank = True, null = True, default = None, help_text="UUID Estatus")
    created_at  = models.DateTimeField(auto_now_add = True)
    update_at   = models.DateTimeField(auto_now = True)