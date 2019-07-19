from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from bbva.backend import models as m
from bbva.backend import serializers as s

# Create your views here.

@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def index(request):
    return Response('Hola mundo')

@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def lista_cuentas(request, dni):
    try:
        cliente = m.Cliente.objects.get(dni=dni)
        lista = m.Cuenta.objects.filter(id_cliente=cliente)
        response = s.CuentaSerializer(lista, many=True)
        return Response(response.data, content_type='application/json')
    except m.Cliente.DoesNotExist:
        return Response('DNI NO REGISTRADO', content_type='application/json')



