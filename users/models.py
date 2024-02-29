import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from catalogs.models import Status
from catalogs.models import Rol

class CustomUser(AbstractUser):
    id              = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    email           = models.EmailField(max_length = 150, unique=True, blank = False, help_text="Email")
    user_rol        = models.ForeignKey(Rol, on_delete = models.CASCADE, blank = True, default = None, null = True, help_text="UUID Rol")
    phone_number    = models.CharField(default = '', blank = True, null = True, help_text="Numero telefonico")
    voice_identifier= models.CharField(max_length = 50, default = '', help_text="Identificador de VoIP")
    profile_picture = models.ImageField(upload_to = 'profile_pics/', default = 'default.png', null = True, blank = True, help_text="Foto de perfil")
    status          = models.ForeignKey(Status, on_delete = models.CASCADE, blank = True, default = None, null = True, help_text="UUID Estatus")
    last_access     = models.DateTimeField(auto_now_add=True, help_text="Fecha ultimo acceso")
    created_at      = models.DateTimeField(auto_now_add=True, help_text="Fecha creacion")
    update_at       = models.DateTimeField(auto_now=True, help_text="Fecha actualizacion")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email.split('@')[0]
        super().save(*args, **kwargs)