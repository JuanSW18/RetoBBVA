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


"""@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def login_get(request):
    #usuario = request.data['usuario']
    #password = request.data['password']
    print(request.data)
    try:
        #user = m.UsuarioBBVA.objects.get(usuario=usuario, password=password)
        return Response('Bienvenido', content_type='application/json')
    except m.UsuarioBBVA.DoesNotExist:
        return Response('USUARIO Y/O CONTRASEÑA INCORRECTOS', content_type='application/json')"""

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
def listar_recibos(request, id_usuario):
    try:
        cliente = m.Cliente.objects.get(id_usuario=id_usuario)
        # agregar id de servicio
        lista = m.Recibo.objects.filter(id_cliente=cliente, estado='No Pagado' or 'Vencido')
        response = s.ReciboSerializer(lista, many=True)
        return Response(response.data, content_type='application/json')
    except m.Cliente.DoesNotExist:
        return Response('ID NO REGISTRADO', content_type='application/json')


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def lista_servicios(request):
    servicios = m.Servicio.objects.all()
    response = s.ServicioSerializer(servicios, many=True)
    return Response(response.data, content_type='application/json')


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def lista_proveedores(request):
    proveedores = m.Proveedor.objects.all()
    response = s.ProveedorSerializer(proveedores, many=True)
    return Response(response.data, content_type='application/json')


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def lista_proveedores2(request, nombre_servicio):
    servicios = m.Servicio.objects.filter(nombre=nombre_servicio)
    lista_servicios = list(servicios)
    lista_proveedores = {}
    for servicio in lista_servicios:
        lista_proveedores[servicio.id_proveedor_id] = servicio.id_proveedor.nombre_proveedor
    return Response(lista_proveedores, content_type='application/json')


@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def pagar_servicio(request):
    id_recibo = request.data['id_recibo']
    id_cuenta_bancaria = request.data['id_cuenta_bancaria']
    try:
        recibo = m.Recibo.objects.get(id_recibo=id_recibo)
        cuenta_bancaria = m.CuentaBancaria.objects.get(id_cuenta_bancaria=id_cuenta_bancaria)
        cuenta_bancaria.saldo = cuenta_bancaria.saldo - recibo.monto
        cuenta_bancaria.save()
        recibo.estado = 'Pagado'
        recibo.save()
        return Response('Recibo pagado!', content_type='application/json')
    except m.Recibo.DoesNotExist or m.CuentaBancaria.DoesNotExist:
        return Response('ERROR!', content_type='application/json')