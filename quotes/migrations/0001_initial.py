# Generated by Django 5.0.1 on 2024-02-18 04:17

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("campaigns", "0001_initial"),
        ("catalogs", "0001_initial"),
        ("companies", "__first__"),
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="QuoteOption",
            fields=[
                (
                    "quote_option_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        help_text="UUID Opcion de cotizacion",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "type_price",
                    models.IntegerField(
                        default=0,
                        help_text="Tipo de precio, ej. 1. Normal, 2. Promocion",
                    ),
                ),
                (
                    "subtotal",
                    models.DecimalField(
                        blank=True,
                        decimal_places=4,
                        default=0,
                        help_text="Subtotal de la opcion $",
                        max_digits=10,
                    ),
                ),
                (
                    "discount",
                    models.DecimalField(
                        blank=True,
                        decimal_places=4,
                        default=0,
                        help_text="Descuento de la opcion $",
                        max_digits=10,
                    ),
                ),
                (
                    "tax",
                    models.DecimalField(
                        blank=True,
                        decimal_places=4,
                        default=0,
                        help_text="Impuesto $",
                        max_digits=10,
                    ),
                ),
                (
                    "total",
                    models.DecimalField(
                        blank=True,
                        decimal_places=4,
                        default=0,
                        help_text="Total $",
                        max_digits=10,
                    ),
                ),
                (
                    "deadline",
                    models.DateTimeField(
                        blank=True,
                        default=None,
                        help_text="Fecha limite de validez del precio",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("update_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="OptionProduct",
            fields=[
                (
                    "option_product_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        help_text="UUID Opcion-Producto",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "quantity",
                    models.IntegerField(default=0, help_text="Cantidad de lugares"),
                ),
                (
                    "price",
                    models.DecimalField(
                        blank=True,
                        decimal_places=4,
                        default=0,
                        help_text="Precio unitario",
                        max_digits=10,
                    ),
                ),
                (
                    "total",
                    models.DecimalField(
                        blank=True,
                        decimal_places=4,
                        default=0,
                        help_text="Precio total",
                        max_digits=10,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("update_at", models.DateTimeField(auto_now=True)),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        help_text="UUID Producto",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        help_text="UUID Estatus",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalogs.status",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Quote",
            fields=[
                (
                    "quote_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        help_text="UUID Cotizacion",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "tax_include",
                    models.BooleanField(default=True, help_text="Incluye impuesto"),
                ),
                (
                    "register_date",
                    models.DateField(
                        blank=True,
                        default=None,
                        help_text="Fecha de registro de cotizacion Front",
                        null=True,
                    ),
                ),
                (
                    "payment_date",
                    models.DateField(
                        blank=True,
                        default=None,
                        help_text="Fecha de pago de cotizacion Front",
                        null=True,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, help_text="Fecha creacion interna de sistema"
                    ),
                ),
                (
                    "update_at",
                    models.DateTimeField(
                        auto_now=True, help_text="Fecha ultima actualizacion"
                    ),
                ),
                (
                    "campaign",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        help_text="UUID Campaing",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="campaigns.campaign",
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        help_text="UUID Empresa",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="companies.company",
                    ),
                ),
                (
                    "contact",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        help_text="UUID Contacto",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="companies.companycontact",
                    ),
                ),
                (
                    "invoice_status",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        help_text="UUID Estatus único de facturación",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="invoice_status",
                        to="catalogs.status",
                    ),
                ),
                (
                    "payment_method",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        help_text="UUID Metodo de pago",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalogs.paymentmethod",
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        help_text="UUID Estatus",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalogs.status",
                    ),
                ),
            ],
        ),
    ]