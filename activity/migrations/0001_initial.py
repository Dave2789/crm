# Generated by Django 5.0.1 on 2024-02-18 04:17

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("catalogs", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Activity",
            fields=[
                (
                    "activity_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        help_text="UUID Actividad",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("update_at", models.DateTimeField(auto_now=True)),
                (
                    "status",
                    models.ForeignKey(
                        blank=True,
                        help_text="UUID Estatus",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalogs.status",
                    ),
                ),
            ],
        ),
    ]
