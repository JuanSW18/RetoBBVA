from rest_framework.serializers import ModelSerializer
from .models import Cliente, Cuenta, Servicio

class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('__all__')


class CuentaSerializer(ModelSerializer):
    class Meta:
        model = Cuenta
        fields = ('__all__')


class ServicioSerializer(ModelSerializer):
    class Meta:
        model = Servicio
        fields = ('__all__')
