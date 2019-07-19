from django.db import models

# Create your models here.

class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    dni = models.CharField(max_length=8)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9)

    class Meta:
        db_table = 'cliente'


class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)

    class Meta:
        db_table = 'servicio'


class Cuenta(models.Model):
    id_cuenta = models.IntegerField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    monto = models.DecimalField(decimal_places=2, max_digits=8)
    estado = models.CharField(max_length=15)
    fecha_vencimiento = models.DateField()
    fecha_pago = models.DateField()

    class Meta:
        db_table = 'cuenta'

