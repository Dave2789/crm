# Generated by Django 5.0.1 on 2024-02-18 04:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("campaigns", "0001_initial"),
        ("catalogs", "0001_initial"),
        ("companies", "__first__"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="campaign",
            name="owner_user",
            field=models.ForeignKey(
                blank=True,
                default=None,
                help_text="UUID Agente/Usuario encargado/principal",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="campaign",
            name="product_category",
            field=models.ForeignKey(
                blank=True,
                default=None,
                help_text="UUID Categoria Producto / Solucion",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="catalogs.productcategory",
            ),
        ),
        migrations.AddField(
            model_name="campaign",
            name="status",
            field=models.ForeignKey(
                blank=True,
                default=None,
                help_text="UUID Estatus",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="catalogs.status",
            ),
        ),
        migrations.AddField(
            model_name="campaigncompany",
            name="campaign",
            field=models.ForeignKey(
                blank=True,
                default=None,
                help_text="UUID Campaign relacionada",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="companies",
                to="campaigns.campaign",
            ),
        ),
        migrations.AddField(
            model_name="campaigncompany",
            name="company",
            field=models.ForeignKey(
                blank=True,
                default=None,
                help_text="UUID Company relacionada",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="companies.company",
            ),
        ),
        migrations.AddField(
            model_name="campaigncompany",
            name="status",
            field=models.ForeignKey(
                blank=True,
                default=None,
                help_text="UUID Estatus",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="catalogs.status",
            ),
        ),
        migrations.AddField(
            model_name="campaignuser",
            name="campaign",
            field=models.ForeignKey(
                blank=True,
                default=None,
                help_text="UUID Campaign relacionada",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="users",
                to="campaigns.campaign",
            ),
        ),
        migrations.AddField(
            model_name="campaignuser",
            name="status",
            field=models.ForeignKey(
                blank=True,
                default=None,
                help_text="UUID Estatus",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="catalogs.status",
            ),
        ),
        migrations.AddField(
            model_name="campaignuser",
            name="user",
            field=models.ForeignKey(
                blank=True,
                default=None,
                help_text="UUID Usuario/Agente relacionado",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
