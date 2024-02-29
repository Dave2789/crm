from .models import Status, TypeActivity
from django.shortcuts import get_object_or_404

#CONSTANTES
STATUS_ACTIVO_DEFAULT               = "00d91403-ffb8-44ca-ab98-96e899925216"
STATUS_ELIMINADO_DEFAULT            = "9d31c5c9-8db6-4c52-b114-0ec0a099cf02"
STATUS_COTIZACION_CREADA            = "5fb730e9-3802-461f-a4f3-592ff04c4387"
STATUS_COTIZACION_RECHAZA_LEAD      = "2b26360a-86c4-4c07-b2c6-0830ae656bcf"
STATUS_COTIZACION_RECHAZA_CLIENTE   = "410eac18-ee07-49bb-bd44-18717470f946"
STATUS_COTIZACION_CANCELADA         = "0830d65c-8fb3-488b-aa3f-56f0ebbd6983"
STATUS_COTIZACION_APROBADA          = "2b95f05d-64d4-4b36-a51c-a3ca7c6bdc72"
STATUS_COTIZACION_APROBADA_PC       = "f4fa3c48-8b48-4d39-ad09-a6699a66459f"
STATUS_COTIZACION_ACEPTADA          = "3944df8e-d359-4569-b712-ea174be69cca"
STATUS_PENDIENTE_FACTURAR           = "84cc6072-f4e0-4780-b87c-49087af2b7e4"
STATUS_FACTURADA                    = "0e202967-7cba-4899-9038-d91b9a14f57e"
STATUS_FACTURADA_EXTERNAMENTE       = "1cb68ab0-8849-4c28-9f4b-9e426d0c0db4"
UUID_PROSPECTO                      = "ec43fa4e-1ade-46ea-9841-1692074ce8cd"
UUID_LEAD                           = "20a3bf77-6669-40ec-b214-e31122d7eb7a"
UUID_CLIENTE                        = "d1203730-3ac8-4f06-b095-3ec56ef3b54d"
TYPE_ACTIVITY_NOTA                  = "1caf1dd4-a844-4469-96ce-ffc1f7fad818"

def get_status_instance(UUID):
    status = get_object_or_404(Status, status_id = UUID)
    return status

def assign_default_status(model_instance, default_status_instance):
    model_instance.status = default_status_instance

def get_type_activity_instance(UUID):
    type_activity = get_object_or_404(TypeActivity, type_activity_id = UUID)
    return type_activity