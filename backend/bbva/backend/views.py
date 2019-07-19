from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def index(request):
    return Response('Hola mundo')
