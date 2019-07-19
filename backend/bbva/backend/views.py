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


@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def login(request):
    serializer = s.UsuarioSerializer(data=request.data)
    if serializer.is_valid():
        usuario = serializer.data['usuario']
        password = serializer.data['password']
        try:
            user = m.UsuarioBBVA.objects.get(usuario=usuario, password=password)
            return Response('Bienvenido', content_type='application/json')
        except m.UsuarioBBVA.DoesNotExist:
            return Response('USUARIO Y/O CONTRASEÑA INCORRECTOS', content_type='application/json')
    else:
        return Response('ERROR', content_type='application/json')


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def get_list_cuentas_bancarias(request, id_usuario):
    try:
        cliente = m.Cliente.objects.get(id_usuario=id_usuario)
        lista_cuentas_bancarias = m.CuentaBancaria.objects.filter(id_cliente=cliente)
        response = s.CuentaBancariaSerializer(lista_cuentas_bancarias, many=True)
        return Response(response.data, content_type='application/json')
    except m.Cliente.DoesNotExist:
        return Response('ID DE USUARIO NO EXISTE', content_type='application/json')

@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def lista_cuentas(request, dni):
    try:
        cliente = m.Cliente.objects.get(dni=dni)
        lista = m.Recibo.objects.filter(id_cliente=cliente)
        response = s.ReciboSerializer(lista, many=True)
        return Response(response.data, content_type='application/json')
    except m.Cliente.DoesNotExist:
        return Response('DNI NO REGISTRADO', content_type='application/json')
