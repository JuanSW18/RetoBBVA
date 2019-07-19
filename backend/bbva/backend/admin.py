from django.contrib import admin
from bbva.backend import models

# Register your models here.
admin.site.register(models.Cliente)
admin.site.register(models.Servicio)
admin.site.register(models.Cuenta)
