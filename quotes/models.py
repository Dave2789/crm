import uuid
from django.db import models
from users.models import CustomUser
from campaigns.models import Campaign
from products.models import Product
from companies.models import Company, CompanyContact
from catalogs.models import Status, PaymentMethod

class Quote(models.Model):
    quote_id    = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, help_text="UUID Cotizacion")
    quote_number = models.IntegerField(unique=True, blank = True, null = True, help_text="Número consecutivo de cotización")
    company     = models.ForeignKey(Company, on_delete = models.CASCADE, default = None, blank = True, null = True, help_text="UUID Empresa")
    contact     = models.ForeignKey(CompanyContact, on_delete = models.CASCADE, default = None, blank = True, null = True, help_text="UUID Contacto")
    user        = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default = None, blank = True, null = True, help_text="UUID usuario")
    campaign    = models.ForeignKey(Campaign, on_delete = models.CASCADE, blank = True, default = None, null = True, help_text="UUID Campaing")
    payment_method  = models.ForeignKey(PaymentMethod, on_delete = models.CASCADE, blank = True, default = None, null = True, help_text="UUID Metodo de pago")
    tax_include     = models.BooleanField(default = True, help_text="Incluye impuesto")
    status          = models.ForeignKey(Status, on_delete = models.CASCADE, blank = True, default = None,  null = True, help_text="UUID Estatus")
    invoice_status  = models.ForeignKey(Status, on_delete=models.CASCADE, blank=True, null=True, default=None, help_text="UUID Estatus único de facturación", related_name='invoice_status')
    register_date   = models.DateTimeField(auto_now_add = True, blank=True, null=True, default = None, help_text="Fecha de registro de cotizacion Front")
    payment_date    = models.DateTimeField(blank=True, null=True, default = None, help_text="Fecha de pago de cotizacion Front")
    invoice_date    = models.DateField(blank=True, null=True, default = None, help_text="Fecha de facturación Front")
    money_in_account    = models.BooleanField(default = False, help_text="Dinero en cuenta")
    quote_total     = models.DecimalField(max_digits = 10, decimal_places = 4, default = 0, blank = True, help_text="Total de la opcion selecionada $")
    created_at      = models.DateTimeField(auto_now_add = True, help_text="Fecha creacion interna de sistema")
    update_at       = models.DateTimeField(auto_now = True, help_text="Fecha ultima actualizacion")

    def save(self, *args, **kwargs):
        if not self.pk:
            last_quote = Quote.objects.order_by('-quote_number').first()
            if last_quote:
                self.quote_number = last_quote.quote_number + 1
            else:
                self.quote_number = 1
        super().save(*args, **kwargs)

class QuoteOption(models.Model):
    quote_option_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, help_text="UUID Opcion de cotizacion")
    quote       = models.ForeignKey(Quote, on_delete = models.CASCADE, blank = True, default = None, null = True, help_text="UUID Cotizacion")
    type_price  = models.IntegerField(default = 0, help_text="Tipo de precio, ej. 1. Normal, 2. Promocion")
    subtotal    = models.DecimalField(max_digits = 10, decimal_places = 4, default = 0, blank = True, help_text="Subtotal de la opcion $")
    discount    = models.DecimalField(max_digits = 10, decimal_places = 4, default = 0, blank = True, help_text="Descuento de la opcion $")
    tax         = models.DecimalField(max_digits = 10, decimal_places = 4, default = 0, blank = True, help_text="Impuesto $")
    total       = models.DecimalField(max_digits = 10, decimal_places = 4, default = 0, blank = True, help_text="Total $")
    deadline    = models.DateTimeField(blank = True, default = None, help_text="Fecha limite de validez del precio")
    selected    = models.BooleanField(default = False, help_text="Opción seleccionada")
    status      = models.ForeignKey(Status, on_delete = models.CASCADE, blank = True, default = None, null = True, help_text="UUID Estatus")
    created_at  = models.DateTimeField(auto_now_add = True)
    update_at   = models.DateTimeField(auto_now = True)

class OptionProduct(models.Model):
    option_product_id   = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, help_text="UUID Opcion-Producto")
    quote_option    = models.ForeignKey(QuoteOption, on_delete = models.CASCADE, blank = True, null = True, default = None, help_text="UUID Opcion de la cotizacion")
    product         = models.ForeignKey(Product, on_delete = models.CASCADE, blank = True, null = True, default = None, help_text="UUID Producto")
    quantity        = models.IntegerField(default = 0, help_text="Cantidad de lugares")
    price           = models.DecimalField(max_digits = 10, decimal_places = 4, default = 0, blank = True, help_text="Precio unitario")
    total           = models.DecimalField(max_digits = 10, decimal_places = 4, default = 0, blank = True, help_text="Precio total")
    status          = models.ForeignKey(Status, on_delete = models.CASCADE, blank = True, null = True, default = None, help_text="UUID Estatus")
    created_at      = models.DateTimeField(auto_now_add = True)
    update_at       = models.DateTimeField(auto_now = True)