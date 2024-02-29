import uuid
from django.db import models
from campaigns.models import Campaign
from catalogs.models import Status, TypeActivity
from companies.models import Company
from users.models import CustomUser

class Activity(models.Model):
    activity_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, help_text="UUID Actividad")
    company     = models.ForeignKey(Company, on_delete=models.CASCADE, blank = True, null = True, default = None, help_text="UUID Company relacionada")
    user        = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank = True, null=True, default = None, help_text="UUID Usuario/Agente relacionado")
    type_activity   = models.ForeignKey(TypeActivity, related_name='activities_type', on_delete = models.CASCADE, blank = True, null = True, default = None, help_text="UUID Actividad")
    campaign        = models.ForeignKey(Campaign, related_name='activities_campaign', on_delete = models.CASCADE, null = True, blank = True, default = None, help_text="UUID Campaign relacionada")
    description     = models.TextField(default = '', help_text="Descripcion de la actividad")
    activity_date   = models.DateField(blank=True, null=True, default = None, help_text="Fecha de la actividad")
    activity_hour   = models.CharField(max_length = 100, default = '', help_text="Hora de la actividad")
    end_date    = models.DateField(blank=True, null=True, help_text="Fecha de finalizacion Front")
    finish      = models.BooleanField(default = False, help_text="Tarea finalizada")
    process     = models.CharField(max_length = 100, default = '', help_text="Proceso/Modulo de la actividad")
    status      = models.ForeignKey(Status, on_delete = models.CASCADE, blank = True, null = True, help_text="UUID Estatus")
    document    = models.FileField(upload_to="documents/", blank = True, default = None)
    created_at  = models.DateTimeField(auto_now_add = True)
    update_at   = models.DateTimeField(auto_now = True)