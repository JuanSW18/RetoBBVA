from django.contrib import admin
from bbva.backend import models

# Register your models here.
admin.site.register(models.UsuarioBBVA)
admin.site.register(models.Cliente)
admin.site.register(models.CuentaBancaria)
admin.site.register(models.Proveedor)
admin.site.register(models.Servicio)
admin.site.register(models.Recibo)
