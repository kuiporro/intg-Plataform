from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status

from crud.models import Donacion, Producto, Usuario, Boleta
from api.serializers import DonacionSerializer, ProductoSerializer, UsuarioSerializer, BoletaSerializer


@csrf_exempt
@api_view(['POST', 'GET'])
def apiBoleta(request):
    if request.method == 'GET':
        boleta = Boleta.objects.all()
        serializer = BoletaSerializer(boleta, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BoletaSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def apiBoletaDetalle(request, buscarId):
    try:
        id = int(buscarId)
        boleta = Boleta.objects.get(pk=id)

    except:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BoletaSerializer(boleta)
        return Response(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BoletaSerializer(boleta, data= data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        boleta.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)   

@csrf_exempt
@api_view(['POST', 'GET'])
def apiDonacion(request):
    if request.method == 'GET':
        donacion = Donacion.objects.all()
        serializer = DonacionSerializer(donacion, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DonacionSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def apiDonacionDetalle(request, buscarId):
    try:
        id = int(buscarId)
        donacion = Donacion.objects.get(pk=id)

    except:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DonacionSerializer(donacion)
        return Response(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DonacionSerializer(donacion, data= data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        donacion.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)   

@csrf_exempt
@api_view(['POST', 'GET'])
def apiProducto(request):
    if request.method == 'GET':
        producto = Producto.objects.all()
        serializer = ProductoSerializer(producto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    
@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def apiProductoDetalle(request, buscarId):
    try:
        id = int(buscarId)
        producto = Producto.objects.get(pk=id)

    except:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(producto, data= data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        producto.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)   

@csrf_exempt
@api_view(['POST', 'GET'])
def apiUsuario(request):
    if request.method == 'GET':
        usuario = Usuario.objects.all()
        serializer = UsuarioSerializer(usuario, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    
@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def apiUsuarioDetalle(request, usrname):
    try:
        usuario = Usuario.objects.get(username=usrname)

    except:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(usuario, data= data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        usuario.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)   

