from django.db import models

# Create your models here.

class UsuarioBBVA(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=15)
    password = models.CharField(max_length=15)

    class Meta:
        db_table = 'usuario'

    def __str__(self):
        return self.usuario


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    id_usuario = models.OneToOneField(UsuarioBBVA, on_delete=models.CASCADE)
    dni = models.CharField(max_length=8)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9)

    class Meta:
        db_table = 'cliente'

    def __str__(self):
        return self.nombres


class CuentaBancaria(models.Model):
    id_cuenta_bancaria = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nro_cuenta = models.CharField(max_length=15)
    saldo = models.DecimalField(decimal_places=2, max_digits=8)

    class Meta:
        db_table = 'cuenta_bancaria'

    def __str__(self):
        return self.nro_cuenta

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=25)
    ruc = models.CharField(max_length=11)

    class Meta:
        db_table = 'proveedor'

    def __str__(self):
        return self.nombre_proveedor

class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=25)

    class Meta:
        db_table = 'servicio'

    def __str__(self):
        return self.nombre

class Recibo(models.Model):
    id_cuenta = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    monto = models.DecimalField(decimal_places=2, max_digits=8)
    ESTADOS = [
        ('Pagado', 'Pagado'),
        ('No Pagado', 'No Pagado'),
        ('Vencido', 'Vencido'),
        ]
    estado = models.CharField(max_length=15,choices = ESTADOS)
    fecha_vencimiento = models.DateField()

    class Meta:
        db_table = 'recibo'

    def __str__(self):
        return str(self.id_cliente) + str(self.id_servicio)
