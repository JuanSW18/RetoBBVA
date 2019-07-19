from rest_framework.serializers import ModelSerializer
from .models import Cliente, Recibo, Servicio, UsuarioBBVA, CuentaBancaria

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = UsuarioBBVA
        fields = ('__all__')


class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('__all__')


class CuentaBancariaSerializer(ModelSerializer):
    class Meta:
        model = CuentaBancaria
        fields = ('__all__')


class ProveedorSerializer(ModelSerializer):
    class Meta:
        model = CuentaBancaria
        fields = ('__all__')


class ServicioSerializer(ModelSerializer):
    class Meta:
        model = Servicio
        fields = ('__all__')


class ReciboSerializer(ModelSerializer):
    class Meta:
        model = Recibo
        fields = ('__all__')
