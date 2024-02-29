import uuid
from django.db import models
from catalogs.models import Country, Currency, Status, ProductCategory
from django.core.validators import MaxValueValidator

class Price(models.Model):
    price_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, help_text="UUID Precio")
    code    = models.CharField(max_length = 100, default = '', help_text="Codigo para identificar")
    price   = models.DecimalField(max_digits = 10, decimal_places = 4, blank = True, help_text="Precio $")
    tax_percentage  = models.IntegerField(default = 0, validators=[MaxValueValidator(99)], help_text="Porcentaje de impuesto")
    currency    = models.ForeignKey(Currency, on_delete = models.CASCADE, blank = True, null = True, default = None, help_text="UUID Currency")
    product_category    = models.ForeignKey(ProductCategory, on_delete = models.CASCADE, blank = True, null = True, default = None, help_text="UUID Categoria de producto")
    status      = models.ForeignKey(Status, on_delete = models.CASCADE, blank = True, null = True, default = None, help_text="UUID Estatus")
    created_at  = models.DateTimeField(auto_now_add = True)
    update_at   = models.DateTimeField(auto_now = True)

class Discount(models.Model):
    discount_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, help_text="UUID Descuento")
    code    = models.CharField(max_length = 100, default = '', help_text="Codigo para identificar")
    name    = models.CharField(max_length = 150, default = '', help_text="Nombre")
    status  = models.ForeignKey(Status, on_delete = models.CASCADE, blank = True, null = True, default = None, help_text="UUID Estatus")
    created_at  = models.DateTimeField(auto_now_add = True)
    update_at   = models.DateTimeField(auto_now = True)

class DiscountScale(models.Model):
    discount_scale_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, help_text="UUID Escala de descuento")
    discount    = models.ForeignKey(Discount, on_delete = models.CASCADE, blank = True, null = True, default = None, help_text="UUID Descuento")
    range_start = models.IntegerField(default = 0, help_text="Rango inicial")
    range_end   = models.IntegerField(default = 0, help_text="Rango final")
    percentage  = models.IntegerField(default = 0, validators=[MaxValueValidator(99)], help_text="Procentaje descuento")
    status      = models.ForeignKey(Status, on_delete = models.CASCADE, blank = True, null = True, default = None, help_text="UUID Estatus")
    created_at  = models.DateTimeField(auto_now_add = True)
    update_at   = models.DateTimeField(auto_now = True)

class Product(models.Model):
    product_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, help_text="UUID Producto")
    product_category    = models.ForeignKey(ProductCategory, on_delete = models.CASCADE, blank = True, null = True, default = None, help_text="UUID Categoria de producto")
    code    = models.CharField(max_length = 100, default = '', help_text="Codigo de producto")
    name    = models.CharField(max_length = 150, default = '', help_text="Nombre del producto")
    country = models.ForeignKey(Country, on_delete = models.CASCADE, blank = True, default = None, null = True, help_text="UUID Pais")
    list_price  = models.DecimalField(max_digits = 10, decimal_places = 4, default = 0, blank = True, help_text="Precio")
    link    = models.URLField(default = '', blank = True, null = True, help_text="Link del producto")
    image   = models.ImageField(upload_to = 'image_products', default = 'default.png', null = True, blank = True, help_text="Imagen del producto")
    price   = models.ForeignKey(Price, on_delete = models.CASCADE, blank = True, default = None, null = True, help_text="UUID Precio")
    discount    = models.ForeignKey(Discount, on_delete = models.CASCADE, blank = True, default = None, null = True, help_text="UUID Descuento")
    status      = models.ForeignKey(Status, on_delete = models.CASCADE, blank = True, default = None, null = True, help_text="UUID Estatus")
    created_at  = models.DateTimeField(auto_now_add = True)
    update_at   = models.DateTimeField(auto_now = True)